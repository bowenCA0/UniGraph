from __future__ import annotations

import io
from dataclasses import dataclass
from typing import Any

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


st.set_page_config(
    page_title="UniGraph Student Plotter",
    page_icon="📊",
    layout="wide",
)


TRANSLATIONS: dict[str, dict[str, str]] = {
    "zh": {
        "language": "语言",
        "app_title": "UniGraph 学生绘图工具",
        "app_subtitle": "导入 Excel 或 CSV，按专业选择绘图和分析方式。",
        "major": "专业",
        "physics": "物理",
        "accounting": "会计",
        "finance": "金融",
        "upload": "导入 Excel 或 CSV 文件",
        "sample": "下载示例 CSV",
        "sheet": "工作表",
        "header": "第一行是列名",
        "preview": "数据预览",
        "raw_preview": "原始位置预览（行列从 1 开始）",
        "plot_setup": "绘图设置",
        "x_axis": "X 轴数据",
        "y_axis": "Y 轴数据",
        "orientation": "方向",
        "vertical": "竖向",
        "horizontal": "横向",
        "start_row": "开始行",
        "start_col": "开始列",
        "end_row": "结束行",
        "end_col": "结束列",
        "chart_type": "图表类型",
        "scatter": "散点图",
        "line": "折线图",
        "bar": "柱状图",
        "histogram": "直方图",
        "pie": "饼图",
        "waterfall": "现金流瀑布图",
        "risk_return": "风险-收益图",
        "portfolio": "资产组合图",
        "cumulative": "累计收益图",
        "correlation": "相关性热力图",
        "show_axes": "显示坐标轴",
        "x_unit": "X 单位",
        "y_unit": "Y 单位",
        "error_bars": "添加 Y 误差棒",
        "fit": "拟合",
        "fit_none": "不拟合",
        "fit_linear": "线性拟合",
        "fit_poly2": "二次拟合",
        "slope": "计算斜率",
        "slope_start": "斜率开始点",
        "slope_end": "斜率结束点",
        "make_plot": "生成图表",
        "generated_code": "生成的 Python 脚本",
        "need_file": "请先上传 CSV 或 Excel 文件。",
        "range_help": "行列编号从 1 开始，和 Excel 里的位置一致。",
        "not_enough": "可用数值点不足，无法绘图。",
        "fit_label": "拟合",
        "slope_label": "斜率",
        "finance_assets": "资产价格或收益列",
        "date_col": "日期列（可选）",
        "risk_note": "金融图默认把选中列作为价格序列，并计算日收益率。",
        "accounting_category": "类别列",
        "accounting_value": "金额列",
        "accounting_note": "会计图适合收入、成本、利润、现金流等科目。",
        "portfolio_weights": "组合权重",
        "select_columns": "选择列",
        "metric": "指标",
        "mean_return": "平均收益",
        "volatility": "波动率",
        "cash_flow": "现金流",
        "manual_xy": "手动 X/Y 绘图",
        "domain_visuals": "专业可视化",
        "y_error": "Y 误差",
        "open_file_warning": "无法读取文件，请确认格式是否正确。",
    },
    "en": {
        "language": "Language",
        "app_title": "UniGraph Student Plotter",
        "app_subtitle": "Import Excel or CSV, then choose discipline-specific plotting tools.",
        "major": "Major",
        "physics": "Physics",
        "accounting": "Accounting",
        "finance": "Finance",
        "upload": "Import Excel or CSV file",
        "sample": "Download sample CSV",
        "sheet": "Sheet",
        "header": "First row contains headers",
        "preview": "Data preview",
        "raw_preview": "Raw position preview (rows and columns start at 1)",
        "plot_setup": "Plot setup",
        "x_axis": "X-axis data",
        "y_axis": "Y-axis data",
        "orientation": "Orientation",
        "vertical": "Vertical",
        "horizontal": "Horizontal",
        "start_row": "Start row",
        "start_col": "Start column",
        "end_row": "End row",
        "end_col": "End column",
        "chart_type": "Chart type",
        "scatter": "Scatter",
        "line": "Line",
        "bar": "Bar",
        "histogram": "Histogram",
        "pie": "Pie chart",
        "waterfall": "Cash-flow waterfall",
        "risk_return": "Risk-return chart",
        "portfolio": "Portfolio chart",
        "cumulative": "Cumulative return chart",
        "correlation": "Correlation heatmap",
        "show_axes": "Show axes",
        "x_unit": "X unit",
        "y_unit": "Y unit",
        "error_bars": "Add Y error bars",
        "fit": "Fit",
        "fit_none": "No fit",
        "fit_linear": "Linear fit",
        "fit_poly2": "Quadratic fit",
        "slope": "Calculate slope",
        "slope_start": "Slope start point",
        "slope_end": "Slope end point",
        "make_plot": "Create chart",
        "generated_code": "Generated Python script",
        "need_file": "Please upload a CSV or Excel file first.",
        "range_help": "Row and column numbers start at 1, matching Excel positions.",
        "not_enough": "Not enough numeric points to plot.",
        "fit_label": "Fit",
        "slope_label": "Slope",
        "finance_assets": "Asset price or return columns",
        "date_col": "Date column (optional)",
        "risk_note": "Finance charts treat selected columns as prices and compute daily returns by default.",
        "accounting_category": "Category column",
        "accounting_value": "Value column",
        "accounting_note": "Accounting charts work well for revenue, cost, profit, and cash-flow accounts.",
        "portfolio_weights": "Portfolio weights",
        "select_columns": "Select columns",
        "metric": "Metric",
        "mean_return": "Mean return",
        "volatility": "Volatility",
        "cash_flow": "Cash flow",
        "manual_xy": "Manual X/Y plot",
        "domain_visuals": "Discipline visuals",
        "y_error": "Y error",
        "open_file_warning": "Could not read the file. Please check the format.",
    },
    "fr": {
        "language": "Langue",
        "app_title": "UniGraph pour étudiants",
        "app_subtitle": "Importez Excel ou CSV, puis choisissez les outils adaptés à la discipline.",
        "major": "Spécialité",
        "physics": "Physique",
        "accounting": "Comptabilité",
        "finance": "Finance",
        "upload": "Importer un fichier Excel ou CSV",
        "sample": "Télécharger un exemple CSV",
        "sheet": "Feuille",
        "header": "La première ligne contient les titres",
        "preview": "Aperçu des données",
        "raw_preview": "Aperçu brut des positions (lignes et colonnes commencent à 1)",
        "plot_setup": "Paramètres du graphique",
        "x_axis": "Données de l'axe X",
        "y_axis": "Données de l'axe Y",
        "orientation": "Orientation",
        "vertical": "Verticale",
        "horizontal": "Horizontale",
        "start_row": "Ligne de début",
        "start_col": "Colonne de début",
        "end_row": "Ligne de fin",
        "end_col": "Colonne de fin",
        "chart_type": "Type de graphique",
        "scatter": "Nuage de points",
        "line": "Courbe",
        "bar": "Barres",
        "histogram": "Histogramme",
        "pie": "Camembert",
        "waterfall": "Cascade de trésorerie",
        "risk_return": "Risque-rendement",
        "portfolio": "Portefeuille",
        "cumulative": "Rendement cumulé",
        "correlation": "Carte de corrélation",
        "show_axes": "Afficher les axes",
        "x_unit": "Unité X",
        "y_unit": "Unité Y",
        "error_bars": "Ajouter les barres d'erreur Y",
        "fit": "Ajustement",
        "fit_none": "Aucun",
        "fit_linear": "Linéaire",
        "fit_poly2": "Quadratique",
        "slope": "Calculer la pente",
        "slope_start": "Début de la pente",
        "slope_end": "Fin de la pente",
        "make_plot": "Créer le graphique",
        "generated_code": "Script Python généré",
        "need_file": "Veuillez d'abord importer un fichier CSV ou Excel.",
        "range_help": "Les numéros de ligne et de colonne commencent à 1, comme dans Excel.",
        "not_enough": "Pas assez de points numériques pour tracer.",
        "fit_label": "Ajustement",
        "slope_label": "Pente",
        "finance_assets": "Colonnes de prix ou rendements",
        "date_col": "Colonne de date (facultatif)",
        "risk_note": "Les graphiques financiers traitent les colonnes choisies comme prix et calculent les rendements quotidiens.",
        "accounting_category": "Colonne de catégorie",
        "accounting_value": "Colonne de montant",
        "accounting_note": "Les graphiques comptables conviennent aux revenus, coûts, profits et flux de trésorerie.",
        "portfolio_weights": "Poids du portefeuille",
        "select_columns": "Choisir les colonnes",
        "metric": "Indicateur",
        "mean_return": "Rendement moyen",
        "volatility": "Volatilité",
        "cash_flow": "Flux de trésorerie",
        "manual_xy": "Graphique X/Y manuel",
        "domain_visuals": "Visualisations spécialisées",
        "y_error": "Erreur Y",
        "open_file_warning": "Impossible de lire le fichier. Vérifiez le format.",
    },
}


LANGUAGE_LABELS = {
    "中文": "zh",
    "English": "en",
    "Français": "fr",
}


@dataclass
class RangeSelection:
    start_row: int
    start_col: int
    end_row: int
    end_col: int
    orientation: str


def t(key: str) -> str:
    language = st.session_state.get("language", "zh")
    return TRANSLATIONS[language].get(key, key)


def make_sample_csv() -> bytes:
    sample = pd.DataFrame(
        {
            "time_s": [0, 1, 2, 3, 4, 5],
            "distance_m": [0.0, 1.1, 4.1, 9.2, 16.1, 25.0],
            "distance_error": [0.1, 0.1, 0.2, 0.2, 0.3, 0.3],
            "Asset_A": [100, 101, 103, 102, 106, 108],
            "Asset_B": [90, 91, 90, 94, 95, 97],
            "account": ["Revenue", "Cost", "Profit", "Operating CF", "Investing CF", "Financing CF"],
            "amount": [1200, -650, 550, 420, -180, 90],
        }
    )
    return sample.to_csv(index=False).encode("utf-8")


def read_csv_bytes(data: bytes, header: int | None) -> pd.DataFrame:
    encodings = ["utf-8-sig", "utf-8", "gbk", "latin1"]
    last_error: Exception | None = None
    for encoding in encodings:
        try:
            return pd.read_csv(io.BytesIO(data), header=header, encoding=encoding)
        except Exception as exc:  # pragma: no cover - Streamlit path
            last_error = exc
    raise last_error or ValueError("Could not read CSV")


def read_uploaded_file(
    file_name: str,
    data: bytes,
    sheet_name: str | None,
    first_row_is_header: bool,
) -> tuple[pd.DataFrame, pd.DataFrame, list[str]]:
    header = 0 if first_row_is_header else None
    suffix = file_name.lower().rsplit(".", 1)[-1]
    if suffix == "csv":
        raw = read_csv_bytes(data, header=None)
        table = read_csv_bytes(data, header=header)
        return raw, table, []

    excel = pd.ExcelFile(io.BytesIO(data))
    sheets = excel.sheet_names
    active_sheet = sheet_name or sheets[0]
    raw = pd.read_excel(io.BytesIO(data), sheet_name=active_sheet, header=None)
    table = pd.read_excel(io.BytesIO(data), sheet_name=active_sheet, header=header)
    return raw, table, sheets


def raw_preview(raw: pd.DataFrame) -> pd.DataFrame:
    preview = raw.copy()
    preview.index = np.arange(1, len(preview) + 1)
    preview.columns = np.arange(1, len(preview.columns) + 1)
    return preview


def coerce_numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce").dropna().reset_index(drop=True)


def extract_series(raw: pd.DataFrame, selection: RangeSelection) -> pd.Series:
    max_row = len(raw)
    max_col = len(raw.columns)
    sr = max(1, min(selection.start_row, max_row))
    er = max(1, min(selection.end_row, max_row))
    sc = max(1, min(selection.start_col, max_col))
    ec = max(1, min(selection.end_col, max_col))
    row_slice = slice(min(sr, er) - 1, max(sr, er))
    col_slice = slice(min(sc, ec) - 1, max(sc, ec))
    block = raw.iloc[row_slice, col_slice]
    if selection.orientation == "horizontal":
        values = block.to_numpy().reshape(-1)
    else:
        values = block.to_numpy().T.reshape(-1)
    return pd.Series(values)


def selection_controls(label: str, raw: pd.DataFrame, prefix: str) -> RangeSelection:
    with st.expander(label, expanded=True):
        st.caption(t("range_help"))
        orientation_label = st.radio(
            t("orientation"),
            options=[t("vertical"), t("horizontal")],
            horizontal=True,
            key=f"{prefix}_orientation_label",
        )
        orientation = "vertical" if orientation_label == t("vertical") else "horizontal"
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            start_row = st.number_input(
                t("start_row"),
                min_value=1,
                max_value=max(1, len(raw)),
                value=1,
                step=1,
                key=f"{prefix}_start_row",
            )
        with c2:
            start_col = st.number_input(
                t("start_col"),
                min_value=1,
                max_value=max(1, len(raw.columns)),
                value=1,
                step=1,
                key=f"{prefix}_start_col",
            )
        with c3:
            default_end_row = min(max(1, len(raw)), 10)
            end_row = st.number_input(
                t("end_row"),
                min_value=1,
                max_value=max(1, len(raw)),
                value=default_end_row,
                step=1,
                key=f"{prefix}_end_row",
            )
        with c4:
            end_col = st.number_input(
                t("end_col"),
                min_value=1,
                max_value=max(1, len(raw.columns)),
                value=1,
                step=1,
                key=f"{prefix}_end_col",
            )
    return RangeSelection(start_row, start_col, end_row, end_col, orientation)


def align_xy(x: pd.Series, y: pd.Series) -> pd.DataFrame:
    length = min(len(x), len(y))
    frame = pd.DataFrame({"x": x.iloc[:length], "y": y.iloc[:length]})
    frame = frame.apply(pd.to_numeric, errors="coerce").dropna()
    return frame.reset_index(drop=True)


def apply_axis_style(fig: go.Figure, show_axes: bool, x_title: str, y_title: str) -> None:
    fig.update_xaxes(visible=show_axes, title=x_title if show_axes else None, zeroline=show_axes)
    fig.update_yaxes(visible=show_axes, title=y_title if show_axes else None, zeroline=show_axes)
    fig.update_layout(
        template="plotly_white",
        margin=dict(l=32, r=24, t=56, b=32),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )


def add_fit_trace(fig: go.Figure, frame: pd.DataFrame, fit_kind: str) -> str | None:
    if fit_kind == "none" or len(frame) < 2:
        return None
    degree = 1 if fit_kind == "linear" else 2
    if len(frame) < degree + 1:
        return None
    coeffs = np.polyfit(frame["x"], frame["y"], degree)
    xs = np.linspace(frame["x"].min(), frame["x"].max(), 100)
    ys = np.polyval(coeffs, xs)
    fig.add_trace(
        go.Scatter(
            x=xs,
            y=ys,
            mode="lines",
            name=t("fit_label"),
            line=dict(width=3, dash="dash"),
        )
    )
    if degree == 1:
        return f"y = {coeffs[0]:.6g}x + {coeffs[1]:.6g}"
    return f"y = {coeffs[0]:.6g}x² + {coeffs[1]:.6g}x + {coeffs[2]:.6g}"


def calculate_slope(frame: pd.DataFrame, start: int, end: int) -> float | None:
    if len(frame) < 2:
        return None
    lo = max(1, min(start, len(frame)))
    hi = max(1, min(end, len(frame)))
    subset = frame.iloc[min(lo, hi) - 1 : max(lo, hi)]
    if len(subset) < 2:
        return None
    coeffs = np.polyfit(subset["x"], subset["y"], 1)
    return float(coeffs[0])


def build_xy_chart(
    frame: pd.DataFrame,
    chart_kind: str,
    show_axes: bool,
    x_unit: str,
    y_unit: str,
    error_y: pd.Series | None,
    fit_kind: str,
) -> tuple[go.Figure, str | None]:
    x_title = "X" + (f" ({x_unit})" if x_unit else "")
    y_title = "Y" + (f" ({y_unit})" if y_unit else "")
    error_values = None
    if error_y is not None:
        errors = coerce_numeric(error_y)
        if len(errors) >= len(frame):
            error_values = errors.iloc[: len(frame)]

    if chart_kind == "line":
        fig = go.Figure(
            go.Scatter(
                x=frame["x"],
                y=frame["y"],
                mode="lines+markers",
                name="data",
                error_y=dict(type="data", array=error_values) if error_values is not None else None,
            )
        )
    elif chart_kind == "bar":
        fig = go.Figure(
            go.Bar(
                x=frame["x"],
                y=frame["y"],
                name="data",
                error_y=dict(type="data", array=error_values) if error_values is not None else None,
            )
        )
    elif chart_kind == "histogram":
        fig = go.Figure(go.Histogram(x=frame["y"], name="data"))
        x_title, y_title = y_title, "Count"
    else:
        fig = go.Figure(
            go.Scatter(
                x=frame["x"],
                y=frame["y"],
                mode="markers",
                name="data",
                marker=dict(size=9),
                error_y=dict(type="data", array=error_values) if error_values is not None else None,
            )
        )

    fit_equation = add_fit_trace(fig, frame, fit_kind)
    apply_axis_style(fig, show_axes, x_title, y_title)
    return fig, fit_equation


def column_options(table: pd.DataFrame) -> list[str]:
    return [str(col) for col in table.columns]


def numeric_table(table: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    selected = table[columns].apply(pd.to_numeric, errors="coerce")
    selected = selected.dropna(how="all")
    return selected


def finance_chart(table: pd.DataFrame) -> go.Figure | None:
    st.info(t("risk_note"))
    columns = column_options(table)
    if not columns:
        return None
    selected = st.multiselect(t("finance_assets"), columns, default=columns[: min(3, len(columns))])
    chart = st.selectbox(
        t("chart_type"),
        [t("risk_return"), t("cumulative"), t("correlation"), t("portfolio")],
    )
    if not selected:
        return None
    data = numeric_table(table, selected)
    if data.empty:
        return None
    returns = data.pct_change(fill_method=None).replace([np.inf, -np.inf], np.nan).dropna(how="all")
    if returns.empty and chart != t("portfolio"):
        return None
    if chart == t("portfolio"):
        st.caption(t("portfolio_weights"))
        weights: dict[str, float] = {}
        weight_cols = st.columns(min(4, len(selected)))
        for index, col in enumerate(selected):
            with weight_cols[index % len(weight_cols)]:
                weights[col] = st.number_input(
                    str(col),
                    min_value=0.0,
                    max_value=1.0,
                    value=round(1 / len(selected), 3),
                    step=0.01,
                    key=f"weight_{col}",
                )
        total = sum(weights.values()) or 1.0
        labels = list(weights.keys())
        values = [value / total for value in weights.values()]
        fig = go.Figure(go.Pie(labels=labels, values=values, hole=0.35))
    elif chart == t("correlation"):
        corr = returns.corr()
        fig = px.imshow(corr, text_auto=".2f", color_continuous_scale="RdBu_r", zmin=-1, zmax=1)
    elif chart == t("cumulative"):
        cumulative = (1 + returns.fillna(0)).cumprod() - 1
        fig = px.line(cumulative, labels={"value": t("mean_return"), "index": "Index"})
    else:
        risk = returns.std()
        reward = returns.mean()
        frame = pd.DataFrame(
            {
                t("volatility"): risk.values,
                t("mean_return"): reward.values,
                "Asset": risk.index.astype(str),
            }
        )
        fig = px.scatter(
            frame,
            x=t("volatility"),
            y=t("mean_return"),
            text="Asset",
            size=np.maximum(np.abs(frame[t("mean_return")]), 0.001),
        )
        fig.update_traces(textposition="top center")
    fig.update_layout(template="plotly_white", margin=dict(l=32, r=24, t=56, b=32))
    return fig


def accounting_chart(table: pd.DataFrame) -> go.Figure | None:
    st.info(t("accounting_note"))
    columns = column_options(table)
    if len(columns) < 2:
        return None
    category = st.selectbox(t("accounting_category"), columns, index=0)
    value_default = 1 if len(columns) > 1 else 0
    value_col = st.selectbox(t("accounting_value"), columns, index=value_default)
    chart = st.selectbox(t("chart_type"), [t("bar"), t("pie"), t("waterfall"), t("line")])
    frame = pd.DataFrame(
        {
            "category": table[category].astype(str),
            "value": pd.to_numeric(table[value_col], errors="coerce"),
        }
    ).dropna()
    if frame.empty:
        return None
    if chart == t("pie"):
        positive = frame.copy()
        positive["value"] = positive["value"].abs()
        fig = px.pie(positive, names="category", values="value")
    elif chart == t("waterfall"):
        fig = go.Figure(
            go.Waterfall(
                x=frame["category"],
                y=frame["value"],
                measure=["relative"] * len(frame),
                connector={"line": {"color": "rgb(80, 80, 80)"}},
            )
        )
    elif chart == t("line"):
        fig = px.line(frame, x="category", y="value", markers=True)
    else:
        fig = px.bar(frame, x="category", y="value")
    fig.update_layout(template="plotly_white", margin=dict(l=32, r=24, t=56, b=32))
    return fig


def generated_script(
    file_name: str,
    chart_kind: str,
    x_selection: RangeSelection,
    y_selection: RangeSelection,
    fit_kind: str,
    x_unit: str,
    y_unit: str,
) -> str:
    return f'''import pandas as pd
import numpy as np
import plotly.graph_objects as go

file_path = "{file_name}"
raw = pd.read_excel(file_path, header=None) if file_path.lower().endswith(("xlsx", "xls")) else pd.read_csv(file_path, header=None)

def extract(raw, start_row, start_col, end_row, end_col, orientation):
    block = raw.iloc[min(start_row, end_row)-1:max(start_row, end_row), min(start_col, end_col)-1:max(start_col, end_col)]
    values = block.to_numpy().reshape(-1) if orientation == "horizontal" else block.to_numpy().T.reshape(-1)
    return pd.to_numeric(pd.Series(values), errors="coerce").dropna().reset_index(drop=True)

x = extract(raw, {x_selection.start_row}, {x_selection.start_col}, {x_selection.end_row}, {x_selection.end_col}, "{x_selection.orientation}")
y = extract(raw, {y_selection.start_row}, {y_selection.start_col}, {y_selection.end_row}, {y_selection.end_col}, "{y_selection.orientation}")
data = pd.DataFrame({{"x": x.iloc[:min(len(x), len(y))], "y": y.iloc[:min(len(x), len(y))]}}).dropna()

mode = "lines+markers" if "{chart_kind}" == "line" else "markers"
fig = go.Figure(go.Scatter(x=data["x"], y=data["y"], mode=mode, name="data"))

if "{fit_kind}" != "none" and len(data) >= 2:
    degree = 1 if "{fit_kind}" == "linear" else 2
    coeffs = np.polyfit(data["x"], data["y"], degree)
    xs = np.linspace(data["x"].min(), data["x"].max(), 100)
    fig.add_trace(go.Scatter(x=xs, y=np.polyval(coeffs, xs), mode="lines", name="fit"))

fig.update_layout(
    template="plotly_white",
    xaxis_title="X{" (" + x_unit + ")" if x_unit else ""}",
    yaxis_title="Y{" (" + y_unit + ")" if y_unit else ""}",
)
fig.show()
'''


def main() -> None:
    with st.sidebar:
        language_label = st.selectbox(t("language"), list(LANGUAGE_LABELS.keys()), index=0)
        st.session_state["language"] = LANGUAGE_LABELS[language_label]
        major_label = st.radio(
            t("major"),
            [t("physics"), t("accounting"), t("finance")],
            horizontal=False,
        )
        first_row_is_header = st.checkbox(t("header"), value=True)
        st.download_button(
            t("sample"),
            data=make_sample_csv(),
            file_name="unigraph_sample.csv",
            mime="text/csv",
        )

    st.title(t("app_title"))
    st.caption(t("app_subtitle"))

    uploaded = st.file_uploader(t("upload"), type=["csv", "xlsx", "xls"])
    if uploaded is None:
        st.warning(t("need_file"))
        return

    data = uploaded.getvalue()
    sheet_name = None
    suffix = uploaded.name.lower().rsplit(".", 1)[-1]
    if suffix != "csv":
        try:
            excel = pd.ExcelFile(io.BytesIO(data))
            sheet_name = st.selectbox(t("sheet"), excel.sheet_names)
        except Exception:
            st.error(t("open_file_warning"))
            return

    try:
        raw, table, _ = read_uploaded_file(uploaded.name, data, sheet_name, first_row_is_header)
    except Exception:
        st.error(t("open_file_warning"))
        return

    tab_plot, tab_data, tab_code = st.tabs([t("plot_setup"), t("preview"), t("generated_code")])

    with tab_data:
        st.subheader(t("preview"))
        st.dataframe(table.head(40), width="stretch")
        st.subheader(t("raw_preview"))
        st.dataframe(raw_preview(raw).head(40), width="stretch")

    major_key = {
        t("physics"): "physics",
        t("accounting"): "accounting",
        t("finance"): "finance",
    }[major_label]

    chart_kind = "scatter"
    x_selection = RangeSelection(1, 1, min(2, len(raw)), 1, "vertical")
    y_selection = RangeSelection(1, min(2, len(raw.columns)), min(2, len(raw)), min(2, len(raw.columns)), "vertical")
    fit_kind = "none"
    x_unit = ""
    y_unit = ""

    with tab_plot:
        chart_options = [t("scatter"), t("line"), t("bar"), t("histogram")]
        if major_key == "accounting":
            mode = st.radio(t("chart_type"), [t("manual_xy"), t("domain_visuals")], horizontal=True)
            if mode == t("domain_visuals"):
                fig = accounting_chart(table)
                if fig is not None:
                    st.plotly_chart(fig, width="stretch")
                else:
                    st.warning(t("not_enough"))
                with tab_code:
                    st.code("# Accounting visualizations use the selected category and value columns.", language="python")
                return
        elif major_key == "finance":
            mode = st.radio(t("chart_type"), [t("manual_xy"), t("domain_visuals")], horizontal=True)
            if mode == t("domain_visuals"):
                fig = finance_chart(table)
                if fig is not None:
                    st.plotly_chart(fig, width="stretch")
                else:
                    st.warning(t("not_enough"))
                with tab_code:
                    st.code("# Finance visualizations use selected asset columns and calculated returns.", language="python")
                return

        chart_label = st.selectbox(t("chart_type"), chart_options)
        chart_kind = {
            t("scatter"): "scatter",
            t("line"): "line",
            t("bar"): "bar",
            t("histogram"): "histogram",
        }[chart_label]
        x_selection = selection_controls(t("x_axis"), raw, "x")
        y_selection = selection_controls(t("y_axis"), raw, "y")

        c1, c2, c3 = st.columns(3)
        with c1:
            show_axes = st.checkbox(t("show_axes"), value=True)
        with c2:
            x_unit = st.text_input(t("x_unit"), value="")
        with c3:
            y_unit = st.text_input(t("y_unit"), value="")

        error_y = None
        if st.checkbox(t("error_bars"), value=False):
            error_selection = selection_controls(t("y_error"), raw, "error")
            error_y = extract_series(raw, error_selection)

        fit_choice = st.selectbox(t("fit"), [t("fit_none"), t("fit_linear"), t("fit_poly2")])
        fit_kind = {
            t("fit_none"): "none",
            t("fit_linear"): "linear",
            t("fit_poly2"): "poly2",
        }[fit_choice]

        x = coerce_numeric(extract_series(raw, x_selection))
        y = coerce_numeric(extract_series(raw, y_selection))
        frame = align_xy(x, y)

        if len(frame) < 2:
            st.warning(t("not_enough"))
            return

        slope_enabled = st.checkbox(t("slope"), value=fit_kind == "linear")
        slope_value = None
        if slope_enabled:
            c4, c5 = st.columns(2)
            with c4:
                slope_start = st.number_input(t("slope_start"), min_value=1, max_value=len(frame), value=1, step=1)
            with c5:
                slope_end = st.number_input(t("slope_end"), min_value=1, max_value=len(frame), value=len(frame), step=1)
            slope_value = calculate_slope(frame, slope_start, slope_end)

        fig, fit_equation = build_xy_chart(
            frame,
            chart_kind,
            show_axes,
            x_unit,
            y_unit,
            error_y,
            fit_kind,
        )
        st.plotly_chart(fig, width="stretch")
        metric_cols = st.columns(3)
        if fit_equation:
            metric_cols[0].metric(t("fit_label"), fit_equation)
        if slope_value is not None:
            metric_cols[1].metric(t("slope_label"), f"{slope_value:.6g}")

    with tab_code:
        st.code(
            generated_script(
                uploaded.name,
                chart_kind if "chart_kind" in locals() else "scatter",
                x_selection if "x_selection" in locals() else RangeSelection(1, 1, 2, 1, "vertical"),
                y_selection if "y_selection" in locals() else RangeSelection(1, 2, 2, 2, "vertical"),
                fit_kind if "fit_kind" in locals() else "none",
                x_unit if "x_unit" in locals() else "",
                y_unit if "y_unit" in locals() else "",
            ),
            language="python",
        )


if __name__ == "__main__":
    main()
