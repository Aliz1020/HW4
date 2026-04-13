import os
import warnings
from datetime import datetime

import pandas as pd
import pingouin as pg
import plotly.express as px

# =========================
# 1. 基礎設定
# =========================
DEFAULT_XLSX_PATH = "MAI_SELF_prepost_filled.xlsx"
RESULTS_DIR = "results"

warnings.filterwarnings("ignore")


def log(msg: str):
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}")


def ensure_dirs():
    """建立結果輸出資料夾"""
    os.makedirs(os.path.join(RESULTS_DIR, "plots"), exist_ok=True)
    os.makedirs(os.path.join(RESULTS_DIR, "stats"), exist_ok=True)


# =========================
# 2. 資料前處理
# =========================
def validate_score_range(df: pd.DataFrame, col: str, min_val: float, max_val: float):
    """檢查分數是否超出合理範圍"""
    bad_mask = (df[col] < min_val) | (df[col] > max_val)
    if bad_mask.any():
        bad_count = int(bad_mask.sum())
        raise ValueError(
            f"欄位 '{col}' 有 {bad_count} 筆資料超出範圍 [{min_val}, {max_val}]。"
        )


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    log("正在清理資料格式...")

    # 去除欄位名稱前後空白
    df.columns = df.columns.str.strip()

    # 對應你目前 Excel 的實際欄位名稱
    expected_cols = ["ID", "Group", "MAI-pre", "MAI-post", "SELF-pre", "SELF-post"]
    missing_cols = [col for col in expected_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"缺少必要欄位: {missing_cols}")

    # 統一 Group 欄位為 0/1
    # 0 = Control, 1 = Experimental
    group_map = {
        "Ctrl": 0,
        "Control": 0,
        "CG": 0,
        "CON": 0,
        "2": 0,
        2: 0,
        "0": 0,
        0: 0,
        "Exp": 1,
        "Experimental": 1,
        "EG": 1,
        "EXP": 1,
        "1": 1,
        1: 1,
    }
    df["Group"] = df["Group"].map(group_map).fillna(df["Group"])

    valid_groups = set(df["Group"].dropna().unique())
    if not valid_groups.issubset({0, 1}):
        raise ValueError(
            f"Group 欄位格式不正確，偵測到的值為: {sorted(valid_groups)}。"
            "請使用 Exp/Control、EXP/CON、1/0 或 2/1 對應格式。"
        )

    # 數值轉換
    numeric_cols = ["MAI-pre", "MAI-post", "SELF-pre", "SELF-post"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # 刪除缺漏值
    before_rows = len(df)
    df = df.dropna(subset=expected_cols).copy()
    after_rows = len(df)

    if before_rows != after_rows:
        log(f"已刪除 {before_rows - after_rows} 筆缺漏資料。")

    # 分數範圍檢查
    validate_score_range(df, "MAI-pre", 0, 100)
    validate_score_range(df, "MAI-post", 0, 100)
    validate_score_range(df, "SELF-pre", 0, 96)
    validate_score_range(df, "SELF-post", 0, 96)

    log(f"資料清理完成，可分析樣本數: {len(df)}")
    return df


# =========================
# 3. 描述統計
# =========================
def save_descriptive_stats(df: pd.DataFrame):
    log("輸出描述統計...")

    group_labels = {0: "Control", 1: "Experimental"}
    df_desc = df.copy()
    df_desc["Group_Label"] = df_desc["Group"].map(group_labels)

    cols = ["MAI-pre", "MAI-post", "SELF-pre", "SELF-post"]
    desc = df_desc.groupby("Group_Label")[cols].agg(["mean", "std", "min", "max", "count"])

    output_path = os.path.join(RESULTS_DIR, "stats", "descriptive_statistics.csv")
    desc.to_csv(output_path, encoding="utf-8-sig")

    print("\n--- Descriptive Statistics ---")
    print(desc)


# =========================
# 4. 獨立樣本 t 檢定（檢查前測是否不顯著）
# =========================
def run_independent_ttest(df: pd.DataFrame, target_name: str, score_col: str):
    log(f"執行 {target_name} 的獨立樣本 t 檢定...")

    try:
        exp_scores = df[df["Group"] == 1][score_col]
        ctrl_scores = df[df["Group"] == 0][score_col]

        res = pg.ttest(exp_scores, ctrl_scores, correction="auto").iloc[0]

        result_df = pd.DataFrame([{
            "Measure": target_name,
            "Score_Column": score_col,
            "T": round(float(res["T"]), 3),
            "dof": round(float(res["dof"]), 3),
            "p-val": round(float(res["p-val"]), 4),
            "cohen-d": round(float(res["cohen-d"]), 4),
            "CI95%": str(res["CI95%"]),
        }])

        output_path = os.path.join(
            RESULTS_DIR, "stats", f"independent_ttest_{target_name.lower()}_{score_col.lower().replace('-', '_')}.csv"
        )
        result_df.to_csv(output_path, index=False, encoding="utf-8-sig")

        print(f"\n--- {target_name} Independent t-test ({score_col}) ---")
        print(result_df)

    except Exception as e:
        log(f"⚠️ {target_name} 獨立樣本 t 檢定執行失敗: {e}")


# =========================
# 5. ANCOVA（控制前測，比較後測）
# =========================
def run_ancova(df: pd.DataFrame, target_name: str, dv_col: str, covar_col: str):
    log(f"執行 {target_name} 的 ANCOVA...")
    try:
        res = pg.ancova(
            data=df,
            dv=dv_col,
            covar=covar_col,
            between="Group"
        )

        output_path = os.path.join(
            RESULTS_DIR, "stats", f"ancova_{target_name.lower()}.csv"
        )
        res.to_csv(output_path, index=False, encoding="utf-8-sig")

        print(f"\n--- {target_name} ANCOVA Result ---")
        print(res)

        fig = px.scatter(
            df,
            x=covar_col,
            y=dv_col,
            color=df["Group"].map({0: "Control", 1: "Experimental"}),
            trendline="ols",
            title=f"{target_name} ANCOVA",
            labels={
                covar_col: f"{target_name} Pre-test",
                dv_col: f"{target_name} Post-test",
                "color": "Group",
            },
        )
        fig.write_html(
            os.path.join(RESULTS_DIR, "plots", f"ancova_{target_name.lower()}.html")
        )

        try:
            fig.write_image(
                os.path.join(RESULTS_DIR, "plots", f"ancova_{target_name.lower()}.png")
            )
        except Exception:
            log(f"{target_name} 圖已輸出 HTML；PNG 未輸出（若需要可安裝 kaleido）。")

    except Exception as e:
        log(f"⚠️ {target_name} ANCOVA 執行失敗: {e}")


# =========================
# 6. 配對樣本 t 檢定（組內前後測）
# =========================
def run_paired_ttest(df: pd.DataFrame, target_name: str, pre_col: str, post_col: str):
    log(f"執行 {target_name} 的組內前後測配對樣本 t 檢定...")

    try:
        rows = []

        for group_value, group_name in [(0, "Control"), (1, "Experimental")]:
            sub = df[df["Group"] == group_value]
            res = pg.ttest(sub[post_col], sub[pre_col], paired=True).iloc[0]

            rows.append({
                "Measure": target_name,
                "Group": group_name,
                "Pre_Column": pre_col,
                "Post_Column": post_col,
                "T": round(float(res["T"]), 3),
                "dof": round(float(res["dof"]), 3),
                "p-val": round(float(res["p-val"]), 4),
                "cohen-d": round(float(res["cohen-d"]), 4),
            })

        result_df = pd.DataFrame(rows)
        output_path = os.path.join(
            RESULTS_DIR, "stats", f"paired_ttest_{target_name.lower()}.csv"
        )
        result_df.to_csv(output_path, index=False, encoding="utf-8-sig")

        print(f"\n--- {target_name} Paired t-test Result ---")
        print(result_df)

    except Exception as e:
        log(f"⚠️ {target_name} 配對樣本 t 檢定執行失敗: {e}")


# =========================
# 7. 整理摘要表
# =========================
def build_summary_table(df: pd.DataFrame):
    log("整理分析摘要表...")

    summary_rows = []

    analyses = [
        ("MAI", "MAI-post", "MAI-pre"),
        ("SELF", "SELF-post", "SELF-pre"),
    ]

    for name, post_col, pre_col in analyses:
        try:
            # 前測獨立樣本 t 檢定
            t_pre = pg.ttest(
                df[df["Group"] == 1][pre_col],
                df[df["Group"] == 0][pre_col],
                correction="auto"
            ).iloc[0]

            # ANCOVA
            ancova_res = pg.ancova(data=df, dv=post_col, covar=pre_col, between="Group")
            group_row = ancova_res[ancova_res["Source"] == "Group"].iloc[0]

            summary_rows.append({
                "Measure": name,
                "Pretest_t": round(float(t_pre["T"]), 3),
                "Pretest_p": round(float(t_pre["p-val"]), 4),
                "ANCOVA_F": round(float(group_row["F"]), 3),
                "ANCOVA_p": round(float(group_row["p-unc"]), 4),
                "Partial_eta_squared": round(float(group_row["np2"]), 4) if "np2" in group_row else None
            })

        except Exception as e:
            summary_rows.append({
                "Measure": name,
                "Pretest_t": "ERROR",
                "Pretest_p": None,
                "ANCOVA_F": str(e),
                "ANCOVA_p": None,
                "Partial_eta_squared": None
            })

    summary_df = pd.DataFrame(summary_rows)
    summary_df.to_csv(
        os.path.join(RESULTS_DIR, "stats", "analysis_summary.csv"),
        index=False,
        encoding="utf-8-sig"
    )

    print("\n--- Analysis Summary ---")
    print(summary_df)


# =========================
# 8. 主程式
# =========================
def main():
    ensure_dirs()
    log("🚀 開始執行後設認知與程式設計自我效能分析...")

    if not os.path.exists(DEFAULT_XLSX_PATH):
        log(f"❌ 找不到檔案: {DEFAULT_XLSX_PATH}")
        log("請把 Excel 檔放在同一個資料夾，並命名為 MAI_SELF_prepost_filled.xlsx")
        return

    df = pd.read_excel(DEFAULT_XLSX_PATH)
    df = preprocess_data(df)

    # 描述統計
    save_descriptive_stats(df)

    # 前測是否不顯著：獨立樣本 t 檢定
    run_independent_ttest(df, "MAI_Pretest", "MAI-pre")
    run_independent_ttest(df, "SELF_Pretest", "SELF-pre")

    # 若你也想直接看後測兩組差異，可保留這兩行
    run_independent_ttest(df, "MAI_Posttest", "MAI-post")
    run_independent_ttest(df, "SELF_Posttest", "SELF-post")

    # ANCOVA：比較兩組後測差異，控制前測
    run_ancova(df, "MAI", "MAI-post", "MAI-pre")
    run_ancova(df, "SELF", "SELF-post", "SELF-pre")

    # 組內前後測變化
    run_paired_ttest(df, "MAI", "MAI-pre", "MAI-post")
    run_paired_ttest(df, "SELF", "SELF-pre", "SELF-post")

    # 摘要表
    build_summary_table(df)

    log(f"🎉 分析完成！所有結果已儲存至 '{RESULTS_DIR}' 資料夾。")


if __name__ == "__main__":
    main()
