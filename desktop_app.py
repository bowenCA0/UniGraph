from __future__ import annotations

import math
import os
import json
import subprocess
import sys
import threading
import urllib.error
import urllib.request
import webbrowser
from dataclasses import dataclass
from pathlib import Path
from tkinter import BooleanVar, DoubleVar, IntVar, StringVar, filedialog, messagebox
import tkinter as tk
from tkinter import colorchooser, ttk

import numpy as np
import pandas as pd
from matplotlib import rcParams
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib.ticker import ScalarFormatter


rcParams["font.sans-serif"] = [
    "Microsoft YaHei",
    "SimHei",
    "Arial Unicode MS",
    "DejaVu Sans",
]
rcParams["axes.unicode_minus"] = False

MAX_PREVIEW_ROWS = 100000
APP_VERSION = "0.1.2"
LOGIN_URL = "https://unigraph.online"
SUPPORT_URL = "https://unigraph.online/support.html"
LATEST_RELEASE_API_URL = "https://api.github.com/repos/bowenCA0/UniGraph/releases/latest"
LATEST_EXE_DOWNLOAD_URL = "https://github.com/bowenCA0/UniGraph/releases/latest/download/UniGraph.exe"


TEXT = {
    "zh": {
        "title": "UniGraph 本地桌面版",
        "language": "语言",
        "major": "专业",
        "physics": "物理",
        "accounting": "会计",
        "finance": "金融",
        "open": "导入 Excel/CSV",
        "no_file": "请先导入 Excel 或 CSV 文件。",
        "file_loaded": "已导入",
        "all_rows_loaded": "已加载全部 {count} 行。",
        "partial_rows_loaded": "已显示前 {shown} 行，还有 {remaining} 行未加载。可点击文件路径用其他工具预览或编辑：",
        "open_file_failed": "无法打开文件，请手动打开该路径。",
        "sheet": "工作表",
        "header": "第一行是列名",
        "mode": "模式",
        "manual": "手动 X/Y 绘图",
        "domain": "专业可视化",
        "x_range": "X 轴范围",
        "y_range": "Y 轴范围",
        "err_range": "误差范围",
        "orientation": "方向",
        "vertical": "竖向",
        "horizontal": "横向",
        "start_row": "开始行",
        "start_col": "开始列",
        "end_row": "结束行",
        "end_col": "结束列",
        "selected_row": "选择行",
        "selected_col": "选择列",
        "chart": "图表",
        "scatter": "散点图",
        "line": "折线图",
        "bar": "柱状图",
        "hist": "直方图",
        "pie": "饼图",
        "waterfall": "现金流瀑布图",
        "risk": "风险-收益图",
        "portfolio": "资产组合图",
        "cumulative": "累计收益图",
        "corr": "相关性热力图",
        "axes": "显示坐标轴",
        "x_unit": "X 单位",
        "y_unit": "Y 单位",
        "error": "Y 误差棒",
        "fit": "拟合",
        "fit_none": "不拟合",
        "fit_linear": "线性拟合",
        "fit_poly2": "二次拟合",
        "slope": "计算斜率",
        "slope_start": "斜率开始点",
        "slope_end": "斜率结束点",
        "plot": "生成图表",
        "preview": "数据预览",
        "raw_preview": "原始位置预览",
        "category": "类别列",
        "value": "金额列",
        "assets": "资产列",
        "status_ready": "准备就绪",
        "not_enough": "数值数据不足，无法绘图。",
        "bad_file": "无法读取文件，请确认格式。",
        "select_assets": "请至少选择一个资产列。",
        "slope_value": "斜率",
        "fit_result": "拟合结果",
        "one_click_analysis": "一键数据分析",
        "analysis_result": "数据分析结果",
        "analysis_need_xy": "请先在手动 X/Y 绘图中选择至少两个有效数值点。",
        "analysis_x_min": "分析 X 最小值",
        "analysis_x_max": "分析 X 最大值",
        "calculate": "计算",
        "apply_to_chart": "应用到原图",
        "add_regression_line": "添加线性回归函数图",
        "show_equation_on_chart": "显示回归方程",
        "show_slope_intercept_on_chart": "显示斜率和截距",
        "show_correlation_on_chart": "显示 r 和 R²",
        "regression_equation": "线性回归方程",
        "correlation_r": "相关系数 r",
        "determination_r2": "决定系数 R²",
        "intercept": "截距",
        "sample_count": "样本数 n",
        "rmse": "均方根误差 RMSE",
        "plot_style": "绘图风格",
        "academic_style": "学术模式",
        "presentation_style": "展示模式",
        "scientific_x": "X 轴科学计数法",
        "scientific_y": "Y 轴科学计数法",
        "plot_title": "图形标题",
        "image_params": "图像参数设置",
        "x_axis_name": "X 轴名称",
        "y_axis_name": "Y 轴名称",
        "data_color": "数据颜色",
        "fit_color": "拟合线颜色",
        "grid_color": "网格颜色",
        "choose_color": "选择颜色",
        "apply": "应用",
        "figure_manager": "图形管理",
        "new_figure": "新建图形",
        "combine_figures": "生成双 Y 轴图",
        "saved_figures": "已保留图形",
        "default_figure_name": "图形 {number}",
        "no_current_plot": "当前没有可保留的手动 X/Y 图形。",
        "figure_saved": "已保留图形",
        "select_two_figures": "请至少选择两张已保留图形进行合并。",
        "combined_title": "双 Y 轴图",
        "right_y_axis": "右 Y 轴",
        "dual_axis_name": "双 Y 轴图名称",
        "choose_dual_axis_figures": "选择要合成双 Y 轴的图形",
        "confirm": "确定",
        "cancel": "取消",
        "delete_figure": "删除图形",
        "confirm_delete_figure": "确定删除“{name}”吗？",
        "figure_deleted": "已删除图形",
        "collapse_left_sidebar": "收起左侧栏",
        "expand_left_sidebar": "展开左侧栏",
        "collapse_right_sidebar": "收起右侧栏",
        "expand_right_sidebar": "展开右侧栏",
        "login": "登录",
        "login_opened": "已打开 UniGraph 在线登录页面",
        "login_failed": "无法打开登录页面，请手动访问 https://unigraph.online",
        "support_author": "支持与打赏作者",
        "support_opened": "已打开支持与打赏页面",
        "support_failed": "无法打开支持页面，请手动访问 https://unigraph.online/support.html",
        "startup_loading": "加载中...",
        "startup_enter": "进入程序",
        "copyright": "版权所有 bowen",
        "update_title": "发现新版本",
        "update_message": "当前版本：{current}\n最新版本：{latest}\n\n是否现在下载更新？",
        "update_now": "更新",
        "update_skip": "跳过",
        "update_opened": "已打开新版下载页面",
        "update_open_failed": "无法打开下载页面，请手动访问 GitHub Release。",
    },
    "en": {
        "title": "UniGraph Desktop",
        "language": "Language",
        "major": "Major",
        "physics": "Physics",
        "accounting": "Accounting",
        "finance": "Finance",
        "open": "Import Excel/CSV",
        "no_file": "Please import an Excel or CSV file first.",
        "file_loaded": "Loaded",
        "all_rows_loaded": "Loaded all {count} rows.",
        "partial_rows_loaded": "Showing the first {shown} rows. {remaining} rows are not loaded. Click the file path to preview or edit in another tool:",
        "open_file_failed": "Could not open this file. Please open the path manually.",
        "sheet": "Sheet",
        "header": "First row has headers",
        "mode": "Mode",
        "manual": "Manual X/Y plot",
        "domain": "Discipline visuals",
        "x_range": "X-axis range",
        "y_range": "Y-axis range",
        "err_range": "Error range",
        "orientation": "Orientation",
        "vertical": "Vertical",
        "horizontal": "Horizontal",
        "start_row": "Start row",
        "start_col": "Start column",
        "end_row": "End row",
        "end_col": "End column",
        "selected_row": "Selected row",
        "selected_col": "Selected column",
        "chart": "Chart",
        "scatter": "Scatter",
        "line": "Line",
        "bar": "Bar",
        "hist": "Histogram",
        "pie": "Pie chart",
        "waterfall": "Cash-flow waterfall",
        "risk": "Risk-return chart",
        "portfolio": "Portfolio chart",
        "cumulative": "Cumulative returns",
        "corr": "Correlation heatmap",
        "axes": "Show axes",
        "x_unit": "X unit",
        "y_unit": "Y unit",
        "error": "Y error bars",
        "fit": "Fit",
        "fit_none": "No fit",
        "fit_linear": "Linear fit",
        "fit_poly2": "Quadratic fit",
        "slope": "Calculate slope",
        "slope_start": "Slope start",
        "slope_end": "Slope end",
        "plot": "Create chart",
        "preview": "Data preview",
        "raw_preview": "Raw position preview",
        "category": "Category column",
        "value": "Value column",
        "assets": "Asset columns",
        "status_ready": "Ready",
        "not_enough": "Not enough numeric data to plot.",
        "bad_file": "Could not read this file. Please check the format.",
        "select_assets": "Select at least one asset column.",
        "slope_value": "Slope",
        "fit_result": "Fit result",
        "one_click_analysis": "One-click analysis",
        "analysis_result": "Data analysis result",
        "analysis_need_xy": "Please select at least two valid numeric points in Manual X/Y plot.",
        "analysis_x_min": "Analysis X min",
        "analysis_x_max": "Analysis X max",
        "calculate": "Calculate",
        "apply_to_chart": "Apply to chart",
        "add_regression_line": "Add linear regression line",
        "show_equation_on_chart": "Show equation",
        "show_slope_intercept_on_chart": "Show slope and intercept",
        "show_correlation_on_chart": "Show r and R²",
        "regression_equation": "Linear regression equation",
        "correlation_r": "Correlation r",
        "determination_r2": "Coefficient R²",
        "intercept": "Intercept",
        "sample_count": "Sample size n",
        "rmse": "RMSE",
        "plot_style": "Plot style",
        "academic_style": "Academic",
        "presentation_style": "Presentation",
        "scientific_x": "Scientific X axis",
        "scientific_y": "Scientific Y axis",
        "plot_title": "Chart title",
        "image_params": "Image parameters",
        "x_axis_name": "X-axis name",
        "y_axis_name": "Y-axis name",
        "data_color": "Data color",
        "fit_color": "Fit line color",
        "grid_color": "Grid color",
        "choose_color": "Choose color",
        "apply": "Apply",
        "figure_manager": "Figure manager",
        "new_figure": "New figure",
        "combine_figures": "Dual Y-axis chart",
        "saved_figures": "Saved figures",
        "default_figure_name": "Figure {number}",
        "no_current_plot": "There is no manual X/Y figure to keep.",
        "figure_saved": "Figure saved",
        "select_two_figures": "Select at least two saved figures to combine.",
        "combined_title": "Dual Y-axis chart",
        "right_y_axis": "Right Y axis",
        "dual_axis_name": "Dual Y-axis chart name",
        "choose_dual_axis_figures": "Choose figures for the dual Y-axis chart",
        "confirm": "OK",
        "cancel": "Cancel",
        "delete_figure": "Delete figure",
        "confirm_delete_figure": "Delete \"{name}\"?",
        "figure_deleted": "Figure deleted",
        "collapse_left_sidebar": "Collapse left sidebar",
        "expand_left_sidebar": "Expand left sidebar",
        "collapse_right_sidebar": "Collapse right sidebar",
        "expand_right_sidebar": "Expand right sidebar",
        "login": "Log in",
        "login_opened": "Opened the UniGraph online login page",
        "login_failed": "Could not open the login page. Please visit https://unigraph.online",
        "support_author": "Support / Tip the author",
        "support_opened": "Opened the support page",
        "support_failed": "Could not open the support page. Please visit https://unigraph.online/support.html",
        "startup_loading": "Loading...",
        "startup_enter": "Enter app",
        "copyright": "Copyright bowen",
        "update_title": "Update available",
        "update_message": "Current version: {current}\nLatest version: {latest}\n\nDownload the update now?",
        "update_now": "Update",
        "update_skip": "Skip",
        "update_opened": "Opened the update download page",
        "update_open_failed": "Could not open the download page. Please visit GitHub Releases manually.",
    },
    "fr": {
        "title": "UniGraph bureau",
        "language": "Langue",
        "major": "Spécialité",
        "physics": "Physique",
        "accounting": "Comptabilité",
        "finance": "Finance",
        "open": "Importer Excel/CSV",
        "no_file": "Importez d'abord un fichier Excel ou CSV.",
        "file_loaded": "Importé",
        "all_rows_loaded": "{count} lignes chargées.",
        "partial_rows_loaded": "{shown} lignes affichées. {remaining} lignes non chargées. Cliquez le chemin du fichier pour l'ouvrir dans un autre outil :",
        "open_file_failed": "Impossible d'ouvrir ce fichier. Ouvrez le chemin manuellement.",
        "sheet": "Feuille",
        "header": "Première ligne avec titres",
        "mode": "Mode",
        "manual": "Graphique X/Y manuel",
        "domain": "Visualisations spécialisées",
        "x_range": "Plage X",
        "y_range": "Plage Y",
        "err_range": "Plage d'erreur",
        "orientation": "Orientation",
        "vertical": "Verticale",
        "horizontal": "Horizontale",
        "start_row": "Ligne début",
        "start_col": "Colonne début",
        "end_row": "Ligne fin",
        "end_col": "Colonne fin",
        "selected_row": "Ligne choisie",
        "selected_col": "Colonne choisie",
        "chart": "Graphique",
        "scatter": "Nuage de points",
        "line": "Courbe",
        "bar": "Barres",
        "hist": "Histogramme",
        "pie": "Camembert",
        "waterfall": "Cascade de trésorerie",
        "risk": "Risque-rendement",
        "portfolio": "Portefeuille",
        "cumulative": "Rendements cumulés",
        "corr": "Carte de corrélation",
        "axes": "Afficher les axes",
        "x_unit": "Unité X",
        "y_unit": "Unité Y",
        "error": "Barres d'erreur Y",
        "fit": "Ajustement",
        "fit_none": "Aucun",
        "fit_linear": "Linéaire",
        "fit_poly2": "Quadratique",
        "slope": "Calculer la pente",
        "slope_start": "Début pente",
        "slope_end": "Fin pente",
        "plot": "Créer",
        "preview": "Aperçu",
        "raw_preview": "Aperçu brut",
        "category": "Colonne catégorie",
        "value": "Colonne montant",
        "assets": "Colonnes d'actifs",
        "status_ready": "Prêt",
        "not_enough": "Pas assez de données numériques.",
        "bad_file": "Impossible de lire ce fichier.",
        "select_assets": "Choisissez au moins une colonne.",
        "slope_value": "Pente",
        "fit_result": "Ajustement",
        "one_click_analysis": "Analyse en un clic",
        "analysis_result": "Résultat de l'analyse",
        "analysis_need_xy": "Choisissez au moins deux points numériques valides en graphique X/Y manuel.",
        "analysis_x_min": "X min d'analyse",
        "analysis_x_max": "X max d'analyse",
        "calculate": "Calculer",
        "apply_to_chart": "Appliquer au graphique",
        "add_regression_line": "Ajouter la droite linéaire",
        "show_equation_on_chart": "Afficher l'équation",
        "show_slope_intercept_on_chart": "Afficher pente et intercept",
        "show_correlation_on_chart": "Afficher r et R²",
        "regression_equation": "Équation linéaire",
        "correlation_r": "Corrélation r",
        "determination_r2": "Coefficient R²",
        "intercept": "Ordonnée à l'origine",
        "sample_count": "Taille n",
        "rmse": "RMSE",
        "plot_style": "Style",
        "academic_style": "Académique",
        "presentation_style": "Présentation",
        "scientific_x": "Axe X scientifique",
        "scientific_y": "Axe Y scientifique",
        "plot_title": "Titre du graphique",
        "image_params": "Paramètres de l'image",
        "x_axis_name": "Nom de l'axe X",
        "y_axis_name": "Nom de l'axe Y",
        "data_color": "Couleur des données",
        "fit_color": "Couleur de l'ajustement",
        "grid_color": "Couleur de la grille",
        "choose_color": "Choisir",
        "apply": "Appliquer",
        "figure_manager": "Gestion des figures",
        "new_figure": "Nouvelle figure",
        "combine_figures": "Double axe Y",
        "saved_figures": "Figures conservées",
        "default_figure_name": "Figure {number}",
        "no_current_plot": "Aucune figure X/Y manuelle à conserver.",
        "figure_saved": "Figure conservée",
        "select_two_figures": "Sélectionnez au moins deux figures.",
        "combined_title": "Graphique à deux axes Y",
        "right_y_axis": "Axe Y droit",
        "dual_axis_name": "Nom du graphique à deux axes Y",
        "choose_dual_axis_figures": "Choisir les figures à combiner",
        "confirm": "OK",
        "cancel": "Annuler",
        "delete_figure": "Supprimer la figure",
        "confirm_delete_figure": "Supprimer « {name} » ?",
        "figure_deleted": "Figure supprimée",
        "collapse_left_sidebar": "Réduire le panneau gauche",
        "expand_left_sidebar": "Afficher le panneau gauche",
        "collapse_right_sidebar": "Réduire le panneau droit",
        "expand_right_sidebar": "Afficher le panneau droit",
        "login": "Connexion",
        "login_opened": "Page de connexion UniGraph ouverte",
        "login_failed": "Impossible d'ouvrir la page. Visitez https://unigraph.online",
        "support_author": "Soutenir l'auteur",
        "support_opened": "Page de soutien ouverte",
        "support_failed": "Impossible d'ouvrir la page. Visitez https://unigraph.online/support.html",
        "startup_loading": "Chargement...",
        "startup_enter": "Ouvrir l'application",
        "copyright": "Copyright bowen",
        "update_title": "Mise à jour disponible",
        "update_message": "Version actuelle : {current}\nDernière version : {latest}\n\nTélécharger la mise à jour maintenant ?",
        "update_now": "Mettre à jour",
        "update_skip": "Ignorer",
        "update_opened": "Page de téléchargement ouverte",
        "update_open_failed": "Impossible d'ouvrir la page. Visitez GitHub Releases manuellement.",
    },
}


LANGUAGES = {"中文": "zh", "English": "en", "Français": "fr"}
LANGUAGE_NAMES = {value: key for key, value in LANGUAGES.items()}


def _config_path() -> Path:
    base = os.environ.get("APPDATA")
    if base:
        return Path(base) / "UniGraph" / "settings.json"
    return Path.home() / ".unigraph" / "settings.json"


def _load_saved_language() -> str:
    try:
        config = json.loads(_config_path().read_text(encoding="utf-8"))
    except Exception:
        return "zh"
    language = str(config.get("language", "zh"))
    return language if language in TEXT else "zh"


def _save_language(language: str) -> None:
    if language not in TEXT:
        return
    try:
        path = _config_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"language": language}, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception:
        pass


def _open_url(url: str) -> bool:
    try:
        return bool(webbrowser.open_new_tab(url))
    except Exception:
        return False


def _version_parts(version: str) -> tuple[int, ...]:
    clean = version.strip().lower().lstrip("v")
    parts: list[int] = []
    for chunk in clean.replace("-", ".").split("."):
        digits = "".join(char for char in chunk if char.isdigit())
        if digits == "":
            break
        parts.append(int(digits))
    return tuple(parts or [0])


def _is_newer_version(latest: str, current: str) -> bool:
    latest_parts = list(_version_parts(latest))
    current_parts = list(_version_parts(current))
    length = max(len(latest_parts), len(current_parts))
    latest_parts.extend([0] * (length - len(latest_parts)))
    current_parts.extend([0] * (length - len(current_parts)))
    return latest_parts > current_parts


def _release_exe_download_url(release: dict[str, object]) -> str:
    assets = release.get("assets")
    if isinstance(assets, list):
        for asset in assets:
            if not isinstance(asset, dict):
                continue
            name = str(asset.get("name", ""))
            if name.lower().endswith(".exe"):
                download_url = str(asset.get("browser_download_url", ""))
                if download_url:
                    return download_url
    return LATEST_EXE_DOWNLOAD_URL


def _center_window(window: tk.Tk | tk.Toplevel, width: int, height: int) -> None:
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = max((screen_width - width) // 2, 0)
    y = max((screen_height - height) // 2, 0)
    window.geometry(f"{width}x{height}+{x}+{y}")


def _run_startup_dialog(saved_language: str) -> str:
    if saved_language not in TEXT:
        saved_language = "zh"

    splash = tk.Tk()
    splash.resizable(False, False)
    selected_language = StringVar(value=saved_language)
    language_name = StringVar(value=LANGUAGE_NAMES.get(saved_language, "中文"))

    container = ttk.Frame(splash, padding=20)
    container.grid(row=0, column=0, sticky="nsew")
    container.columnconfigure(0, weight=1)

    title_label = ttk.Label(container, text="UniGraph", font=("Microsoft YaHei", 20, "bold"), anchor="center")
    title_label.grid(row=0, column=0, sticky="ew", pady=(0, 12))

    loading_label = ttk.Label(container, anchor="center")
    loading_label.grid(row=1, column=0, sticky="ew")

    progress = ttk.Progressbar(container, mode="indeterminate")
    progress.grid(row=2, column=0, sticky="ew", pady=(8, 14))
    progress.start(12)

    language_frame = ttk.Frame(container)
    language_frame.grid(row=3, column=0, sticky="ew", pady=(0, 12))
    language_frame.columnconfigure(1, weight=1)
    language_label = ttk.Label(language_frame)
    language_label.grid(row=0, column=0, sticky="w", padx=(0, 8))
    language_combo = ttk.Combobox(
        language_frame,
        textvariable=language_name,
        values=list(LANGUAGES.keys()),
        state="readonly",
        width=18,
    )
    language_combo.grid(row=0, column=1, sticky="ew")

    button_frame = ttk.Frame(container)
    button_frame.grid(row=4, column=0, sticky="ew")
    button_frame.columnconfigure((0, 1, 2), weight=1)
    login_button = ttk.Button(button_frame, command=lambda: _startup_open_url(splash, selected_language.get(), LOGIN_URL, "login_failed"))
    login_button.grid(row=0, column=0, sticky="ew", padx=(0, 6))
    support_button = ttk.Button(button_frame, command=lambda: _startup_open_url(splash, selected_language.get(), SUPPORT_URL, "support_failed"))
    support_button.grid(row=0, column=1, sticky="ew", padx=6)
    enter_button = ttk.Button(button_frame)
    enter_button.grid(row=0, column=2, sticky="ew", padx=(6, 0))

    copyright_label = ttk.Label(container, anchor="center")
    copyright_label.grid(row=5, column=0, sticky="ew", pady=(16, 0))

    def refresh_text(_event: object | None = None) -> None:
        language = LANGUAGES.get(language_name.get(), selected_language.get())
        selected_language.set(language)
        splash.title(TEXT[language]["title"])
        language_label.configure(text=TEXT[language]["language"])
        loading_label.configure(text=TEXT[language]["startup_loading"])
        login_button.configure(text=TEXT[language]["login"])
        support_button.configure(text=TEXT[language]["support_author"])
        enter_button.configure(text=TEXT[language]["startup_enter"])
        copyright_label.configure(text=TEXT[language]["copyright"])

    def enter_app() -> None:
        language = selected_language.get()
        _save_language(language)
        progress.start(8)
        enter_button.configure(state="disabled")
        loading_label.configure(text=TEXT[language]["startup_loading"])
        splash.after(250, splash.destroy)

    language_combo.bind("<<ComboboxSelected>>", refresh_text)
    enter_button.configure(command=enter_app)
    splash.protocol("WM_DELETE_WINDOW", enter_app)
    refresh_text()
    _center_window(splash, 440, 260)
    splash.mainloop()
    return selected_language.get()


def _startup_open_url(parent: tk.Tk, language: str, url: str, failure_key: str) -> None:
    if language not in TEXT:
        language = "zh"
    if not _open_url(url):
        messagebox.showerror(TEXT[language]["title"], TEXT[language][failure_key], parent=parent)


@dataclass
class RangeControls:
    start_row: IntVar
    start_col: IntVar
    end_row: IntVar
    end_col: IntVar
    orientation: StringVar


@dataclass
class SavedPlot:
    name: str
    data: pd.DataFrame
    kind: str
    x_label: str
    y_label: str
    title: str
    sheet: str
    parts: list["SavedPlot"] | None = None


class UniGraphDesktop(tk.Tk):
    def __init__(self, initial_language: str = "zh") -> None:
        super().__init__()
        if initial_language not in TEXT:
            initial_language = "zh"
        self.lang = StringVar(value=initial_language)
        self.major = StringVar(value="physics")
        self.mode = StringVar(value="manual")
        self.file_path: Path | None = None
        self.raw = pd.DataFrame()
        self.table = pd.DataFrame()
        self.sheet_names: list[str] = []
        self.sheet = StringVar(value="")
        self.first_row_header = BooleanVar(value=True)
        self.preview_note = StringVar(value="")
        self.raw_note = StringVar(value="")
        self.file_link_text = StringVar(value="")

        self.chart_kind = StringVar(value="scatter")
        self.show_axes = BooleanVar(value=True)
        self.use_error = BooleanVar(value=False)
        self.fit_kind = StringVar(value="none")
        self.use_slope = BooleanVar(value=False)
        self.slope_start = IntVar(value=1)
        self.slope_end = IntVar(value=2)
        self.x_unit = StringVar(value="")
        self.y_unit = StringVar(value="")
        self.x_axis_name = StringVar(value="X")
        self.y_axis_name = StringVar(value="Y")
        self.data_color = StringVar(value="#1f77b4")
        self.fit_color = StringVar(value="#111111")
        self.grid_color = StringVar(value="#d0d0d0")
        self.plot_style = StringVar(value="academic")
        self.scientific_x = BooleanVar(value=False)
        self.scientific_y = BooleanVar(value=False)
        self.plot_title = StringVar(value="")
        self.current_plot: SavedPlot | None = None
        self.saved_plots: list[SavedPlot] = []
        self.active_plot_index: int | None = None
        self.context_plot_index: int | None = None
        self.left_sidebar_collapsed = False
        self.right_sidebar_collapsed = False
        self.left_sidebar_width = 380
        self.right_sidebar_width = 190

        self.category_col = StringVar(value="")
        self.value_col = StringVar(value="")
        self.domain_chart = StringVar(value="bar")
        self.status = StringVar(value=self.txt("status_ready"))

        self.x_range = self._range_defaults()
        self.y_range = self._range_defaults(col=2)
        self.err_range = self._range_defaults(col=3)

        self._configure_window()
        self._configure_styles()
        self._build_ui()
        self._refresh_text()
        self.after(1200, self.check_for_updates_async)

    def txt(self, key: str) -> str:
        return TEXT[self.lang.get()].get(key, key)

    def _range_defaults(self, col: int = 1) -> RangeControls:
        return RangeControls(
            start_row=IntVar(value=1),
            start_col=IntVar(value=col),
            end_row=IntVar(value=10),
            end_col=IntVar(value=col),
            orientation=StringVar(value="vertical"),
        )

    def _reset_xy_range_defaults(self) -> None:
        self.x_range.orientation.set("vertical")
        self.y_range.orientation.set("vertical")
        self.err_range.orientation.set("vertical")
        self.x_range.start_col.set(1)
        self.x_range.end_col.set(1)
        self.y_range.start_col.set(2)
        self.y_range.end_col.set(2)
        self.err_range.start_col.set(3)
        self.err_range.end_col.set(3)

    def _configure_window(self) -> None:
        self.title(self.txt("title"))
        self.geometry("1280x820")
        self.minsize(1080, 700)
        self.configure(bg="#eef2f7")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)

    def _configure_styles(self) -> None:
        self.palette = {
            "activity": "#e8edf5",
            "sidebar": "#f8fafc",
            "panel": "#ffffff",
            "main": "#eef2f7",
            "surface": "#ffffff",
            "text": "#1f2937",
            "muted": "#64748b",
            "dark_border": "#d8e0ea",
            "light_border": "#d6dde8",
            "accent": "#2563eb",
            "accent_hover": "#1d4ed8",
            "soft_accent": "#eff6ff",
        }
        style = ttk.Style(self)
        theme_names = set(style.theme_names())
        for theme_name in ("vista", "winnative", "xpnative", "default", "clam"):
            if theme_name in theme_names:
                try:
                    style.theme_use(theme_name)
                    break
                except tk.TclError:
                    continue
        style.configure(".", font=("Microsoft YaHei", 10))
        style.configure("App.TFrame", background=self.palette["main"])
        style.configure("Sidebar.TFrame", background=self.palette["sidebar"])
        style.configure("Activity.TFrame", background=self.palette["activity"])
        style.configure("Panel.TFrame", background=self.palette["panel"])
        style.configure("Main.TFrame", background=self.palette["main"])
        style.configure("Chart.TFrame", background=self.palette["surface"])
        style.configure("Sidebar.TLabel", background=self.palette["sidebar"], foreground=self.palette["text"])
        style.configure("Sidebar.TCheckbutton", background=self.palette["sidebar"], foreground=self.palette["text"])
        style.map("Sidebar.TCheckbutton", background=[("active", self.palette["sidebar"])])
        style.configure("Sidebar.TLabelframe", background=self.palette["sidebar"], foreground=self.palette["text"], bordercolor=self.palette["dark_border"], relief="solid")
        style.configure("Sidebar.TLabelframe.Label", background=self.palette["sidebar"], foreground=self.palette["text"], font=("Microsoft YaHei", 10, "bold"))
        style.configure(
            "Primary.TButton",
            background="#ffffff",
            foreground="#0f172a",
            borderwidth=1,
            bordercolor=self.palette["accent"],
            focusthickness=0,
            padding=(12, 8),
        )
        style.map(
            "Primary.TButton",
            background=[("active", self.palette["soft_accent"]), ("pressed", "#dbeafe"), ("disabled", "#f8fafc")],
            foreground=[("active", "#0f172a"), ("pressed", "#0f172a"), ("disabled", "#64748b")],
            bordercolor=[("active", self.palette["accent"]), ("pressed", self.palette["accent"])],
        )
        style.configure("Sidebar.TButton", background="#ffffff", foreground=self.palette["text"], borderwidth=1, bordercolor=self.palette["dark_border"], padding=(10, 7))
        style.map(
            "Sidebar.TButton",
            background=[("active", self.palette["soft_accent"]), ("pressed", "#dbeafe"), ("disabled", "#f8fafc")],
            foreground=[("active", self.palette["text"]), ("pressed", self.palette["text"]), ("disabled", "#64748b")],
            bordercolor=[("active", self.palette["accent"])],
        )
        style.configure("Collapse.TButton", background=self.palette["activity"], foreground=self.palette["muted"], borderwidth=0, padding=(6, 5))
        style.map("Collapse.TButton", background=[("active", "#dbe3ef")], foreground=[("active", self.palette["accent"])])
        style.configure("Main.TLabel", background=self.palette["main"], foreground="#243042")
        style.configure("Chart.TLabel", background=self.palette["surface"], foreground="#243042")
        style.configure("Chart.TButton", background="#ffffff", foreground="#243042", borderwidth=1, bordercolor=self.palette["light_border"], padding=(10, 6))
        style.map("Chart.TButton", background=[("active", "#eef4ff")], bordercolor=[("active", self.palette["accent"])])
        style.configure("Chart.TRadiobutton", background=self.palette["surface"], foreground="#243042")
        style.configure("Chart.TCheckbutton", background=self.palette["surface"], foreground="#243042")
        style.configure("Status.TLabel", background="#eef2f7", foreground="#445065")
        style.configure("TNotebook", background=self.palette["main"], borderwidth=0)
        style.configure("TNotebook.Tab", padding=(14, 8), background="#e6ebf2", foreground="#4a5568")
        style.map("TNotebook.Tab", background=[("selected", "#ffffff"), ("active", "#f4f7fb")], foreground=[("selected", "#111827")])
        style.configure("Treeview", background="#ffffff", fieldbackground="#ffffff", foreground="#1f2937", bordercolor=self.palette["light_border"], rowheight=28)
        style.configure("Treeview.Heading", background="#edf2f7", foreground="#273449", font=("Microsoft YaHei", 10, "bold"))
        style.map("Treeview", background=[("selected", "#dbeafe")], foreground=[("selected", "#111827")])
        style.configure("TCombobox", fieldbackground="#ffffff", background="#ffffff", foreground="#111827", bordercolor=self.palette["light_border"])
        style.configure("TSpinbox", fieldbackground="#ffffff", foreground="#111827", bordercolor=self.palette["light_border"])

    def _build_ui(self) -> None:
        self.layout_pane = tk.PanedWindow(
            self,
            orient=tk.HORIZONTAL,
            sashwidth=6,
            sashrelief=tk.FLAT,
            bd=0,
            bg=self.palette["activity"],
            showhandle=False,
        )
        self.layout_pane.grid(row=0, column=0, sticky="nsew")

        self.left_shell = ttk.Frame(self.layout_pane, style="Activity.TFrame")
        self.left_shell.columnconfigure(0, weight=1)
        self.left_shell.rowconfigure(1, weight=1)
        self.left_toggle_button = ttk.Button(self.left_shell, command=self._toggle_left_sidebar, style="Collapse.TButton")
        self.left_toggle_button.grid(row=0, column=0, sticky="ew", padx=4, pady=(4, 0))

        self.controls = ttk.Frame(self.left_shell, padding=12, style="Sidebar.TFrame")
        self.controls.grid(row=1, column=0, sticky="nsew")
        self.controls.columnconfigure(0, weight=1)
        self.controls.columnconfigure(1, weight=0)
        self.controls.rowconfigure(10, weight=1)

        self.main_area = ttk.Frame(self.layout_pane, padding=(0, 12, 12, 12), style="Main.TFrame")
        self.main_area.rowconfigure(0, weight=1)
        self.main_area.columnconfigure(0, weight=1)

        self.right_shell = ttk.Frame(self.layout_pane, style="Activity.TFrame")
        self.right_shell.columnconfigure(0, weight=1)
        self.right_shell.rowconfigure(1, weight=1)
        self.right_toggle_button = ttk.Button(self.right_shell, command=self._toggle_right_sidebar, style="Collapse.TButton")
        self.right_toggle_button.grid(row=0, column=0, sticky="ew", padx=4, pady=(4, 0))

        self._build_controls()
        self._build_plot_area()
        self._build_saved_plots_sidebar()

        self.layout_pane.add(self.left_shell, minsize=220, width=self.left_sidebar_width)
        self.layout_pane.add(self.main_area, minsize=520, stretch="always")
        self.layout_pane.add(self.right_shell, minsize=140, width=self.right_sidebar_width)

        status_bar = ttk.Label(self, textvariable=self.status, anchor="w", padding=(12, 6), style="Status.TLabel")
        status_bar.grid(row=1, column=0, sticky="ew")

    def _build_controls(self) -> None:
        self.language_label = ttk.Label(self.controls, style="Sidebar.TLabel")
        self.language_label.grid(row=0, column=0, sticky="w")
        self.language_combo = ttk.Combobox(
            self.controls,
            state="readonly",
            values=list(LANGUAGES.keys()),
            width=24,
        )
        self.language_combo.set(LANGUAGE_NAMES.get(self.lang.get(), "中文"))
        self.language_combo.grid(row=1, column=0, sticky="ew", pady=(2, 10))
        self.language_combo.bind("<<ComboboxSelected>>", self._on_language)
        self._disable_mousewheel_value_change(self.language_combo)

        self.major_label = ttk.Label(self.controls, style="Sidebar.TLabel")
        self.major_label.grid(row=2, column=0, sticky="w")
        self.major_combo = ttk.Combobox(self.controls, state="readonly", width=24)
        self.major_combo.grid(row=3, column=0, sticky="ew", pady=(2, 10))
        self.major_combo.bind("<<ComboboxSelected>>", self._on_major_label)
        self._disable_mousewheel_value_change(self.major_combo)

        self.open_button = self._primary_button(self.controls, command=self.open_file)
        self.open_button.grid(row=4, column=0, sticky="ew", pady=(0, 8))
        self.header_check = ttk.Checkbutton(
            self.controls,
            variable=self.first_row_header,
            command=self.reload_file,
            style="Sidebar.TCheckbutton",
        )
        self.header_check.grid(row=5, column=0, sticky="w", pady=(0, 8))

        self.sheet_label = ttk.Label(self.controls, style="Sidebar.TLabel")
        self.sheet_label.grid(row=6, column=0, sticky="w")
        self.sheet_combo = ttk.Combobox(self.controls, textvariable=self.sheet, state="readonly", width=24)
        self.sheet_combo.grid(row=7, column=0, sticky="ew", pady=(2, 10))
        self.sheet_combo.bind("<<ComboboxSelected>>", lambda _event: self.reload_file())
        self._disable_mousewheel_value_change(self.sheet_combo)

        self.mode_label = ttk.Label(self.controls, style="Sidebar.TLabel")
        self.mode_label.grid(row=8, column=0, sticky="w")
        self.mode_combo = ttk.Combobox(self.controls, state="readonly", width=24)
        self.mode_combo.grid(row=9, column=0, sticky="ew", pady=(2, 10))
        self.mode_combo.bind("<<ComboboxSelected>>", self._on_mode_label)
        self._disable_mousewheel_value_change(self.mode_combo)

        self.form_canvas = tk.Canvas(self.controls, width=340, highlightthickness=0, bg=self.palette["sidebar"])
        self.form_canvas.grid(row=10, column=0, sticky="nsew")
        self.form_scrollbar = ttk.Scrollbar(self.controls, orient="vertical", command=self.form_canvas.yview)
        self.form_scrollbar.grid(row=10, column=1, sticky="ns")
        self.form_canvas.configure(yscrollcommand=self.form_scrollbar.set)

        self.form = ttk.Frame(self.form_canvas, style="Sidebar.TFrame")
        self.form.columnconfigure(0, weight=1)
        self.form_window = self.form_canvas.create_window((0, 0), window=self.form, anchor="nw")
        self.form.bind("<Configure>", self._sync_form_scroll)
        self.form_canvas.bind("<Configure>", self._sync_form_width)
        self.form_canvas.bind("<Enter>", lambda _event: self.form_canvas.bind_all("<MouseWheel>", self._on_form_mousewheel))
        self.form_canvas.bind("<Leave>", lambda _event: self.form_canvas.unbind_all("<MouseWheel>"))

        self.figure_actions = ttk.LabelFrame(self.controls, padding=8, style="Sidebar.TLabelframe")
        self.figure_actions.grid(row=11, column=0, columnspan=2, sticky="ew", pady=(12, 0))
        self.figure_actions.columnconfigure(0, weight=1)
        self.plot_button = self._primary_button(self.figure_actions, command=self.plot)
        self.plot_button.grid(row=0, column=0, sticky="ew")

    def _build_plot_area(self) -> None:
        self.notebook = ttk.Notebook(self.main_area)
        self.notebook.grid(row=0, column=0, sticky="nsew")

        self.chart_tab = ttk.Frame(self.notebook, style="Chart.TFrame")
        self.preview_tab = ttk.Frame(self.notebook, style="Chart.TFrame")
        self.raw_tab = ttk.Frame(self.notebook, style="Chart.TFrame")
        self.notebook.add(self.chart_tab, text=self.txt("chart"))
        self.notebook.add(self.preview_tab, text=self.txt("preview"))
        self.notebook.add(self.raw_tab, text=self.txt("raw_preview"))

        self.chart_tab.rowconfigure(1, weight=1)
        self.chart_tab.columnconfigure(0, weight=1)
        self.chart_options = ttk.Frame(self.chart_tab, padding=(10, 8), style="Chart.TFrame")
        self.chart_options.grid(row=0, column=0, sticky="ew")
        self.chart_options.columnconfigure(1, weight=1)
        self.chart_options.columnconfigure(7, weight=1)
        self.image_params_button = ttk.Button(self.chart_options, command=self.open_image_params_dialog, style="Chart.TButton")
        self.image_params_button.grid(row=0, column=0, sticky="w", pady=(0, 6))
        self.support_button = ttk.Button(self.chart_options, command=self.open_support_page, style="Chart.TButton")
        self.support_button.grid(row=0, column=7, sticky="e", pady=(0, 6), padx=(10, 0))
        self.login_button = self._primary_button(self.chart_options, command=self.open_login_page)
        self.login_button.grid(row=0, column=8, sticky="e", pady=(0, 6), padx=(10, 0))
        self.plot_style_label = ttk.Label(self.chart_options, style="Main.TLabel")
        self.plot_style_label.grid(row=1, column=0, sticky="w", padx=(0, 8))
        self.academic_radio = ttk.Radiobutton(
            self.chart_options,
            variable=self.plot_style,
            value="academic",
            command=self._refresh_plot_if_ready,
            style="Chart.TRadiobutton",
        )
        self.academic_radio.grid(row=1, column=1, sticky="w", padx=(0, 8))
        self.presentation_radio = ttk.Radiobutton(
            self.chart_options,
            variable=self.plot_style,
            value="presentation",
            command=self._refresh_plot_if_ready,
            style="Chart.TRadiobutton",
        )
        self.presentation_radio.grid(row=1, column=2, sticky="w", padx=(0, 18))
        self.scientific_x_check = ttk.Checkbutton(
            self.chart_options,
            variable=self.scientific_x,
            command=self._refresh_plot_if_ready,
            style="Chart.TCheckbutton",
        )
        self.scientific_x_check.grid(row=1, column=3, sticky="w", padx=(0, 10))
        self.scientific_y_check = ttk.Checkbutton(
            self.chart_options,
            variable=self.scientific_y,
            command=self._refresh_plot_if_ready,
            style="Chart.TCheckbutton",
        )
        self.scientific_y_check.grid(row=1, column=4, sticky="w", padx=(0, 10))

        self.figure = Figure(figsize=(8, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.chart_tab)
        self.canvas.get_tk_widget().grid(row=1, column=0, sticky="nsew")
        toolbar = NavigationToolbar2Tk(self.canvas, self.chart_tab, pack_toolbar=False)
        toolbar.update()
        toolbar.grid(row=2, column=0, sticky="ew")

        self.preview_tree = self._make_tree(self.preview_tab, self.preview_note)
        self.raw_tree = self._make_tree(self.raw_tab, self.raw_note)

    def _build_saved_plots_sidebar(self) -> None:
        self.figure_manager = ttk.LabelFrame(self.right_shell, padding=10, style="Sidebar.TLabelframe")
        self.figure_manager.grid(row=1, column=0, sticky="nsew", padx=(0, 12), pady=(4, 12))
        self.figure_manager.rowconfigure(3, weight=1)
        self.figure_manager.columnconfigure(0, weight=1)
        self.new_plot_button = self._primary_button(self.figure_manager, command=self.new_figure)
        self.new_plot_button.grid(row=0, column=0, columnspan=2, sticky="ew", pady=(0, 6))
        self.combine_plot_button = ttk.Button(self.figure_manager, command=self.combine_selected_plots, style="Sidebar.TButton")
        self.combine_plot_button.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(0, 10))
        self.saved_plots_label = ttk.Label(self.figure_manager, style="Sidebar.TLabel")
        self.saved_plots_label.grid(row=2, column=0, sticky="w", pady=(0, 6))
        self.saved_plots_list = tk.Listbox(
            self.figure_manager,
            selectmode="browse",
            width=20,
            exportselection=False,
            activestyle="dotbox",
            bg="#ffffff",
            fg=self.palette["text"],
            selectbackground="#dbeafe",
            selectforeground="#0f172a",
            highlightthickness=1,
            highlightbackground=self.palette["dark_border"],
            highlightcolor=self.palette["accent"],
            relief="flat",
            borderwidth=0,
        )
        self.saved_plots_list.grid(row=3, column=0, sticky="nsew")
        yscroll = ttk.Scrollbar(self.figure_manager, orient="vertical", command=self.saved_plots_list.yview)
        yscroll.grid(row=3, column=1, sticky="ns")
        self.saved_plots_list.configure(yscrollcommand=yscroll.set)
        self.saved_plots_list.bind("<<ListboxSelect>>", self._on_saved_plot_selected)
        self.saved_plots_list.bind("<Double-Button-1>", self._on_saved_plot_selected)
        self._build_saved_plot_context_menu()

    def _build_saved_plot_context_menu(self) -> None:
        self.saved_plot_menu = tk.Menu(self, tearoff=False)
        self.saved_plot_menu.add_command(
            label=self.txt("delete_figure"),
            command=self._delete_context_saved_plot,
        )
        self.saved_plots_list.bind("<Button-3>", self._show_saved_plot_menu)
        self.saved_plots_list.bind("<Control-Button-1>", self._show_saved_plot_menu)
        self.saved_plots_list.bind("<Button-2>", self._show_saved_plot_menu)

    def _show_saved_plot_menu(self, event: tk.Event) -> str | None:
        if self.saved_plots_list.size() == 0:
            return "break"
        index = self.saved_plots_list.nearest(event.y)
        bbox = self.saved_plots_list.bbox(index)
        if bbox is None:
            return "break"
        _x, y, _width, height = bbox
        if event.y < y or event.y > y + height:
            return "break"
        self.context_plot_index = index
        self._select_saved_plot(index)
        self.show_saved_plot(index)
        self.saved_plot_menu.entryconfigure(0, label=self.txt("delete_figure"))
        try:
            self.saved_plot_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.saved_plot_menu.grab_release()
        return "break"

    def _delete_context_saved_plot(self) -> None:
        if self.context_plot_index is None:
            return
        self.delete_saved_plot(self.context_plot_index)

    def _toggle_left_sidebar(self) -> None:
        self._set_sidebar_collapsed("left", not self.left_sidebar_collapsed)

    def _toggle_right_sidebar(self) -> None:
        self._set_sidebar_collapsed("right", not self.right_sidebar_collapsed)

    def _set_sidebar_collapsed(self, side: str, collapsed: bool) -> None:
        if side == "left":
            shell = self.left_shell
            body = self.controls
            expanded_minsize = 220
            collapsed_width = 42
            if collapsed and not self.left_sidebar_collapsed:
                width = shell.winfo_width()
                if width > collapsed_width:
                    self.left_sidebar_width = width
                body.grid_remove()
                self.left_sidebar_collapsed = True
                self.layout_pane.paneconfigure(shell, minsize=collapsed_width, width=collapsed_width)
                self.status.set(self.txt("collapse_left_sidebar"))
            elif not collapsed and self.left_sidebar_collapsed:
                self.left_sidebar_collapsed = False
                body.grid()
                width = max(self.left_sidebar_width, expanded_minsize)
                self.layout_pane.paneconfigure(shell, minsize=expanded_minsize, width=width)
                self.status.set(self.txt("expand_left_sidebar"))
        elif side == "right":
            shell = self.right_shell
            body = self.figure_manager
            expanded_minsize = 140
            collapsed_width = 42
            if collapsed and not self.right_sidebar_collapsed:
                width = shell.winfo_width()
                if width > collapsed_width:
                    self.right_sidebar_width = width
                body.grid_remove()
                self.right_sidebar_collapsed = True
                self.layout_pane.paneconfigure(shell, minsize=collapsed_width, width=collapsed_width)
                self.status.set(self.txt("collapse_right_sidebar"))
            elif not collapsed and self.right_sidebar_collapsed:
                self.right_sidebar_collapsed = False
                body.grid()
                width = max(self.right_sidebar_width, expanded_minsize)
                self.layout_pane.paneconfigure(shell, minsize=expanded_minsize, width=width)
                self.status.set(self.txt("expand_right_sidebar"))
        self._refresh_sidebar_toggle_texts()

    def _refresh_sidebar_toggle_texts(self) -> None:
        left_text = ">" if self.left_sidebar_collapsed else self.txt("collapse_left_sidebar")
        right_text = "<" if self.right_sidebar_collapsed else self.txt("collapse_right_sidebar")
        self.left_toggle_button.configure(text=left_text)
        self.right_toggle_button.configure(text=right_text)

    def _make_tree(self, parent: ttk.Frame, note_var: StringVar) -> ttk.Treeview:
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        tree = ttk.Treeview(parent, show="headings")
        tree.grid(row=0, column=0, sticky="nsew")
        yscroll = ttk.Scrollbar(parent, orient="vertical", command=tree.yview)
        yscroll.grid(row=0, column=1, sticky="ns")
        xscroll = ttk.Scrollbar(parent, orient="horizontal", command=tree.xview)
        xscroll.grid(row=1, column=0, sticky="ew")
        tree.configure(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

        footer = ttk.Frame(parent, padding=(4, 6))
        footer.grid(row=2, column=0, columnspan=2, sticky="ew")
        footer.columnconfigure(1, weight=1)
        ttk.Label(footer, textvariable=note_var, anchor="w").grid(row=0, column=0, sticky="w")
        file_link = ttk.Label(
            footer,
            textvariable=self.file_link_text,
            foreground="#0066cc",
            cursor="hand2",
            anchor="w",
        )
        file_link.grid(row=0, column=1, sticky="ew", padx=(6, 0))
        file_link.bind("<Button-1>", lambda _event: self.open_source_file())
        return tree

    def _sync_form_scroll(self, _event: object | None = None) -> None:
        self.form_canvas.configure(scrollregion=self.form_canvas.bbox("all"))

    def _sync_form_width(self, event: tk.Event) -> None:
        self.form_canvas.itemconfigure(self.form_window, width=event.width)

    def _on_form_mousewheel(self, event: tk.Event) -> None:
        self.form_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _block_mousewheel(self, _event: tk.Event) -> str:
        return "break"

    def _disable_mousewheel_value_change(self, widget: tk.Widget) -> None:
        widget.bind("<MouseWheel>", self._block_mousewheel)
        widget.bind("<Button-4>", self._block_mousewheel)
        widget.bind("<Button-5>", self._block_mousewheel)

    def _int_entry(self, parent: tk.Widget, variable: IntVar, width: int = 8) -> ttk.Entry:
        entry = ttk.Entry(parent, textvariable=variable, width=width)
        self._disable_mousewheel_value_change(entry)
        return entry

    def _primary_button(self, parent: tk.Widget, command: object | None = None) -> tk.Button:
        return tk.Button(
            parent,
            command=command,
            bg=self.palette["accent"],
            fg="#ffffff",
            activebackground=self.palette["accent_hover"],
            activeforeground="#ffffff",
            disabledforeground="#dbeafe",
            relief="flat",
            borderwidth=0,
            highlightthickness=0,
            padx=12,
            pady=7,
            cursor="hand2",
            font=("Microsoft YaHei", 10),
        )

    def _clear_form(self) -> None:
        for child in self.form.winfo_children():
            child.destroy()
        for name in ("asset_list", "category_combo", "value_combo"):
            if hasattr(self, name):
                delattr(self, name)

    def _polish_sidebar_widgets(self, parent: tk.Widget | None = None) -> None:
        parent = parent or self.form
        for child in parent.winfo_children():
            cls = child.winfo_class()
            try:
                if cls == "TLabel":
                    child.configure(style="Sidebar.TLabel")
                elif cls == "TCheckbutton":
                    child.configure(style="Sidebar.TCheckbutton")
                elif cls == "TButton":
                    child.configure(style="Sidebar.TButton")
                elif cls == "TLabelframe":
                    child.configure(style="Sidebar.TLabelframe")
                elif cls == "TFrame":
                    child.configure(style="Sidebar.TFrame")
                elif cls == "TCombobox":
                    self._disable_mousewheel_value_change(child)
                elif isinstance(child, tk.Listbox):
                    child.configure(
                        bg="#ffffff",
                        fg=self.palette["text"],
                        selectbackground="#dbeafe",
                        selectforeground="#0f172a",
                        highlightthickness=1,
                        highlightbackground=self.palette["dark_border"],
                        highlightcolor=self.palette["accent"],
                        relief="flat",
                        borderwidth=0,
                    )
            except tk.TclError:
                pass
            self._polish_sidebar_widgets(child)

    def _build_manual_form(self) -> None:
        self._clear_form()
        row = 0
        self.chart_label = ttk.Label(self.form, text=self.txt("chart"))
        self.chart_label.grid(row=row, column=0, sticky="w")
        row += 1
        chart_items = self._available_chart_items(include_domain=True)
        chart_labels = [label for label, _key in chart_items]
        chart_keys = [key for _label, key in chart_items]
        selected_key = self.chart_kind.get()
        if selected_key not in chart_keys:
            selected_key = "scatter"
        self.chart_combo = ttk.Combobox(
            self.form,
            state="readonly",
            values=chart_labels,
            width=24,
        )
        self.chart_combo.current(chart_keys.index(selected_key))
        self.chart_combo.grid(row=row, column=0, sticky="ew", pady=(2, 8))
        self.chart_combo.bind("<<ComboboxSelected>>", self._on_chart_label)
        row += 1

        row = self._range_frame(self.form, row, self.txt("x_range"), self.x_range)
        row = self._range_frame(self.form, row, self.txt("y_range"), self.y_range)

        self.axes_check = ttk.Checkbutton(self.form, text=self.txt("axes"), variable=self.show_axes)
        self.axes_check.grid(row=row, column=0, sticky="w", pady=(4, 4))
        row += 1

        unit_frame = ttk.Frame(self.form)
        unit_frame.grid(row=row, column=0, sticky="ew", pady=(2, 8))
        unit_frame.columnconfigure((0, 1), weight=1)
        ttk.Label(unit_frame, text=self.txt("x_unit")).grid(row=0, column=0, sticky="w")
        ttk.Label(unit_frame, text=self.txt("y_unit")).grid(row=0, column=1, sticky="w")
        ttk.Entry(unit_frame, textvariable=self.x_unit, width=10).grid(row=1, column=0, sticky="ew", padx=(0, 4))
        ttk.Entry(unit_frame, textvariable=self.y_unit, width=10).grid(row=1, column=1, sticky="ew", padx=(4, 0))
        row += 1

        self.error_check = ttk.Checkbutton(self.form, text=self.txt("error"), variable=self.use_error, command=self._build_manual_form)
        self.error_check.grid(row=row, column=0, sticky="w", pady=(2, 4))
        row += 1
        if self.use_error.get():
            row = self._range_frame(self.form, row, self.txt("err_range"), self.err_range)

        self.fit_label = ttk.Label(self.form, text=self.txt("fit"))
        self.fit_label.grid(row=row, column=0, sticky="w")
        row += 1
        self.fit_combo = ttk.Combobox(
            self.form,
            state="readonly",
            values=[self.txt("fit_none"), self.txt("fit_linear"), self.txt("fit_poly2")],
            width=24,
        )
        self.fit_combo.current(["none", "linear", "poly2"].index(self.fit_kind.get()))
        self.fit_combo.grid(row=row, column=0, sticky="ew", pady=(2, 8))
        self.fit_combo.bind("<<ComboboxSelected>>", self._on_fit_label)
        row += 1

        self.slope_check = ttk.Checkbutton(self.form, text=self.txt("slope"), variable=self.use_slope)
        self.slope_check.grid(row=row, column=0, sticky="w", pady=(2, 4))
        row += 1
        slope_frame = ttk.Frame(self.form)
        slope_frame.grid(row=row, column=0, sticky="ew")
        slope_frame.columnconfigure((0, 1), weight=1)
        ttk.Label(slope_frame, text=self.txt("slope_start")).grid(row=0, column=0, sticky="w")
        ttk.Label(slope_frame, text=self.txt("slope_end")).grid(row=0, column=1, sticky="w")
        self._int_entry(slope_frame, self.slope_start, width=8).grid(row=1, column=0, sticky="ew", padx=(0, 4))
        self._int_entry(slope_frame, self.slope_end, width=8).grid(row=1, column=1, sticky="ew", padx=(4, 0))
        row += 1

        self.analysis_button = self._primary_button(self.form, command=self.analyze_current_xy_data)
        self.analysis_button.configure(text=self.txt("one_click_analysis"))
        self.analysis_button.grid(row=row, column=0, sticky="ew", pady=(10, 0))
        self._polish_sidebar_widgets()

    def _available_chart_items(self, include_domain: bool) -> list[tuple[str, str]]:
        items = [
            (self.txt("scatter"), "scatter"),
            (self.txt("line"), "line"),
            (self.txt("bar"), "bar"),
            (self.txt("hist"), "hist"),
        ]
        if not include_domain:
            return items
        if self.major.get() == "accounting":
            items.extend([(self.txt("pie"), "pie"), (self.txt("waterfall"), "waterfall")])
        elif self.major.get() == "finance":
            items.extend(
                [
                    (self.txt("risk"), "risk"),
                    (self.txt("portfolio"), "portfolio"),
                    (self.txt("cumulative"), "cumulative"),
                    (self.txt("corr"), "corr"),
                ]
            )
        return items

    def _range_frame(self, parent: ttk.Frame, row: int, title: str, controls: RangeControls) -> int:
        frame = ttk.LabelFrame(parent, text=title, padding=8)
        frame.grid(row=row, column=0, sticky="ew", pady=(0, 8))
        frame.columnconfigure((0, 1), weight=1)
        ttk.Label(frame, text=self.txt("orientation")).grid(row=0, column=0, sticky="w")
        combo = ttk.Combobox(frame, state="readonly", values=[self.txt("vertical"), self.txt("horizontal")], width=12)
        combo.current(0 if controls.orientation.get() == "vertical" else 1)
        combo.grid(row=0, column=1, sticky="ew", padx=(6, 0))
        combo.bind("<<ComboboxSelected>>", lambda event, item=controls: self._set_range_orientation(item, event.widget.current()))
        self._disable_mousewheel_value_change(combo)

        if controls.orientation.get() == "vertical":
            fields = [
                (self.txt("selected_col"), controls.start_col),
                (self.txt("start_row"), controls.start_row),
                (self.txt("end_row"), controls.end_row),
            ]
        else:
            fields = [
                (self.txt("selected_row"), controls.start_row),
                (self.txt("start_col"), controls.start_col),
                (self.txt("end_col"), controls.end_col),
            ]
        for index, (label, variable) in enumerate(fields):
            r = 1 + index // 2 * 2
            c = index % 2
            ttk.Label(frame, text=label).grid(row=r, column=c, sticky="w", pady=(6, 0))
            self._int_entry(frame, variable, width=8).grid(row=r + 1, column=c, sticky="ew", padx=(0 if c == 0 else 6, 6 if c == 0 else 0))
        return row + 1

    def _set_range_orientation(self, controls: RangeControls, selected_index: int) -> None:
        controls.orientation.set("vertical" if selected_index == 0 else "horizontal")
        if controls.orientation.get() == "vertical":
            controls.end_col.set(controls.start_col.get())
        else:
            controls.end_row.set(controls.start_row.get())
        self._build_manual_form()

    def _build_domain_form(self) -> None:
        self._clear_form()
        if self.major.get() == "finance":
            chart_items = [(self.txt("risk"), "risk"), (self.txt("portfolio"), "portfolio"), (self.txt("cumulative"), "cumulative"), (self.txt("corr"), "corr")]
        else:
            chart_items = [(self.txt("bar"), "bar"), (self.txt("pie"), "pie"), (self.txt("waterfall"), "waterfall"), (self.txt("line"), "line")]
        charts = [label for label, _key in chart_items]
        keys = [key for _label, key in chart_items]
        selected_key = self.domain_chart.get()
        if selected_key not in keys:
            selected_key = keys[0]

        ttk.Label(self.form, text=self.txt("chart")).grid(row=0, column=0, sticky="w")
        combo = ttk.Combobox(self.form, state="readonly", values=charts, width=24)
        combo.current(keys.index(selected_key))
        combo.grid(row=1, column=0, sticky="ew", pady=(2, 10))
        combo.bind("<<ComboboxSelected>>", self._on_domain_chart_label)
        self.domain_chart.set(selected_key)

        if self.major.get() == "finance":
            ttk.Label(self.form, text=self.txt("assets")).grid(row=2, column=0, sticky="w")
            self.asset_list = tk.Listbox(self.form, selectmode="multiple", height=8, exportselection=False)
            self.asset_list.grid(row=3, column=0, sticky="ew", pady=(2, 8))
            self._fill_asset_list()
        else:
            ttk.Label(self.form, text=self.txt("category")).grid(row=2, column=0, sticky="w")
            self.category_combo = ttk.Combobox(self.form, textvariable=self.category_col, state="readonly", width=24)
            self.category_combo.grid(row=3, column=0, sticky="ew", pady=(2, 8))
            ttk.Label(self.form, text=self.txt("value")).grid(row=4, column=0, sticky="w")
            self.value_combo = ttk.Combobox(self.form, textvariable=self.value_col, state="readonly", width=24)
            self.value_combo.grid(row=5, column=0, sticky="ew", pady=(2, 8))
            self._fill_column_combos()
        self._polish_sidebar_widgets()

    def _refresh_text(self) -> None:
        self.title(self.txt("title"))
        self.language_label.configure(text=self.txt("language"))
        self.major_label.configure(text=self.txt("major"))
        self.open_button.configure(text=self.txt("open"))
        self.header_check.configure(text=self.txt("header"))
        self.sheet_label.configure(text=self.txt("sheet"))
        self.mode_label.configure(text=self.txt("mode"))
        self.figure_actions.configure(text=self.txt("figure_manager"))
        self.figure_manager.configure(text=self.txt("saved_figures"))
        self.plot_button.configure(text=self.txt("plot"))
        self.new_plot_button.configure(text=self.txt("new_figure"))
        self.combine_plot_button.configure(text=self.txt("combine_figures"))
        self.saved_plots_label.configure(text=self.txt("saved_figures"))
        self._refresh_sidebar_toggle_texts()
        self.saved_plot_menu.entryconfigure(0, label=self.txt("delete_figure"))
        self.image_params_button.configure(text=self.txt("image_params"))
        self.support_button.configure(text=self.txt("support_author"))
        self.login_button.configure(text=self.txt("login"))
        self.plot_style_label.configure(text=self.txt("plot_style"))
        self.academic_radio.configure(text=self.txt("academic_style"))
        self.presentation_radio.configure(text=self.txt("presentation_style"))
        self.scientific_x_check.configure(text=self.txt("scientific_x"))
        self.scientific_y_check.configure(text=self.txt("scientific_y"))
        self.notebook.tab(0, text=self.txt("chart"))
        self.notebook.tab(1, text=self.txt("preview"))
        self.notebook.tab(2, text=self.txt("raw_preview"))

        major_values = [self.txt("physics"), self.txt("accounting"), self.txt("finance")]
        self.major_combo.configure(values=major_values)
        self.major_combo.current(["physics", "accounting", "finance"].index(self.major.get()))

        mode_values = [self.txt("manual"), self.txt("domain")]
        self.mode_combo.configure(values=mode_values)
        self.mode_combo.current(0 if self.mode.get() == "manual" else 1)

        if self.mode.get() == "domain" and self.major.get() != "physics":
            self._build_domain_form()
        else:
            self.mode.set("manual")
            self._build_manual_form()

    def _on_language(self, _event: object) -> None:
        self.lang.set(LANGUAGES[self.language_combo.get()])
        _save_language(self.lang.get())
        self._refresh_text()
        self.status.set(self.txt("status_ready"))

    def _on_major_label(self, _event: object) -> None:
        label = self.major_combo.get()
        reverse = {self.txt("physics"): "physics", self.txt("accounting"): "accounting", self.txt("finance"): "finance"}
        self.major.set(reverse[label])
        if self.major.get() == "physics":
            self.mode.set("manual")
        self._refresh_text()

    def _on_mode_label(self, _event: object) -> None:
        self.mode.set("manual" if self.mode_combo.current() == 0 else "domain")
        if self.major.get() == "physics":
            self.mode.set("manual")
        self._refresh_text()

    def _on_chart_label(self, _event: object) -> None:
        chart_items = self._available_chart_items(include_domain=True)
        selected_key = chart_items[self.chart_combo.current()][1]
        if selected_key in {"pie", "waterfall", "risk", "portfolio", "cumulative", "corr"}:
            self.domain_chart.set(selected_key)
            self.mode.set("domain")
            self._refresh_text()
            return
        self.chart_kind.set(selected_key)
        self.mode.set("manual")

    def _on_fit_label(self, _event: object) -> None:
        self.fit_kind.set(["none", "linear", "poly2"][self.fit_combo.current()])

    def _on_domain_chart_label(self, event: object) -> None:
        self.domain_chart.set(self._domain_chart_key(event.widget.get()))

    def _domain_chart_key(self, label: str) -> str:
        mapping = {
            self.txt("bar"): "bar",
            self.txt("pie"): "pie",
            self.txt("waterfall"): "waterfall",
            self.txt("line"): "line",
            self.txt("risk"): "risk",
            self.txt("portfolio"): "portfolio",
            self.txt("cumulative"): "cumulative",
            self.txt("corr"): "corr",
        }
        return mapping.get(label, "bar")

    def open_file(self) -> None:
        path = filedialog.askopenfilename(
            title=self.txt("open"),
            filetypes=[("Data files", "*.csv *.xlsx *.xls"), ("CSV", "*.csv"), ("Excel", "*.xlsx *.xls")],
        )
        if not path:
            return
        self.file_path = Path(path)
        self.reload_file(load_sheets=True)

    def reload_file(self, load_sheets: bool = False) -> None:
        if self.file_path is None:
            return
        try:
            suffix = self.file_path.suffix.lower()
            header = 0 if self.first_row_header.get() else None
            if suffix == ".csv":
                self.sheet_names = []
                self.sheet_combo.configure(values=[])
                self.raw = self._read_csv(header=None)
                self.table = self._read_csv(header=header)
            else:
                if load_sheets or not self.sheet_names:
                    excel = pd.ExcelFile(self.file_path)
                    self.sheet_names = excel.sheet_names
                    self.sheet_combo.configure(values=self.sheet_names)
                    self.sheet.set(self.sheet_names[0])
                self.raw = pd.read_excel(self.file_path, sheet_name=self.sheet.get(), header=None)
                self.table = pd.read_excel(self.file_path, sheet_name=self.sheet.get(), header=header)
        except Exception as exc:
            messagebox.showerror(self.txt("title"), f"{self.txt('bad_file')}\n{exc}")
            return

        self._after_data_loaded()

    def _read_csv(self, header: int | None) -> pd.DataFrame:
        last_error: Exception | None = None
        for encoding in ["utf-8-sig", "utf-8", "gbk", "latin1"]:
            try:
                return pd.read_csv(self.file_path, header=header, encoding=encoding)
            except Exception as exc:
                last_error = exc
        raise last_error or ValueError("CSV read failed")

    def _after_data_loaded(self) -> None:
        row_count = max(1, len(self.raw))
        col_count = max(1, len(self.raw.columns))
        self._reset_xy_range_defaults()
        self.x_range.end_row.set(min(row_count, 10))
        self.y_range.start_col.set(min(2, col_count))
        self.y_range.end_col.set(min(2, col_count))
        self.y_range.end_row.set(min(row_count, 10))
        self.err_range.start_col.set(min(3, col_count))
        self.err_range.end_col.set(min(3, col_count))
        self.err_range.end_row.set(min(row_count, 10))
        self.slope_end.set(min(row_count, 10))
        self._fill_tables()
        self._fill_column_combos()
        self._fill_asset_list()
        if self.file_path is not None:
            self.status.set(f"{self.txt('file_loaded')}: {self.file_path.name}")

    def _fill_tables(self) -> None:
        table_preview, table_remaining = self._preview_slice(self.table)
        self._fill_tree(self.preview_tree, table_preview)
        self.preview_note.set(self._preview_note(len(self.table), len(table_preview), table_remaining))

        raw_preview, raw_remaining = self._preview_slice(self.raw)
        raw = raw_preview.copy()
        raw.index = np.arange(1, len(raw) + 1)
        raw.columns = [str(i) for i in range(1, len(raw.columns) + 1)]
        self._fill_tree(self.raw_tree, raw.reset_index(names="#"))
        self.raw_note.set(self._preview_note(len(self.raw), len(raw_preview), raw_remaining))
        self.file_link_text.set(str(self.file_path) if self.file_path else "")

    def _preview_slice(self, frame: pd.DataFrame) -> tuple[pd.DataFrame, int]:
        if len(frame) <= MAX_PREVIEW_ROWS:
            return frame, 0
        return frame.head(MAX_PREVIEW_ROWS), len(frame) - MAX_PREVIEW_ROWS

    def _preview_note(self, total: int, shown: int, remaining: int) -> str:
        if remaining <= 0:
            return self.txt("all_rows_loaded").format(count=total)
        return self.txt("partial_rows_loaded").format(shown=shown, remaining=remaining)

    def open_source_file(self) -> None:
        if self.file_path is None:
            return
        try:
            if sys.platform.startswith("win"):
                os.startfile(self.file_path)  # type: ignore[attr-defined]
            elif sys.platform == "darwin":
                subprocess.Popen(["open", str(self.file_path)])
            else:
                subprocess.Popen(["xdg-open", str(self.file_path)])
        except Exception:
            messagebox.showerror(self.txt("title"), f"{self.txt('open_file_failed')}\n{self.file_path}")

    def open_login_page(self) -> None:
        opened = _open_url(LOGIN_URL)
        if opened:
            self.status.set(self.txt("login_opened"))
        else:
            messagebox.showerror(self.txt("title"), self.txt("login_failed"))

    def open_support_page(self) -> None:
        opened = _open_url(SUPPORT_URL)
        if opened:
            self.status.set(self.txt("support_opened"))
        else:
            messagebox.showerror(self.txt("title"), self.txt("support_failed"))

    def check_for_updates_async(self) -> None:
        worker = threading.Thread(target=self._check_for_updates_worker, daemon=True)
        worker.start()

    def _check_for_updates_worker(self) -> None:
        request = urllib.request.Request(
            LATEST_RELEASE_API_URL,
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": f"UniGraph/{APP_VERSION}",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=4) as response:
                payload = response.read(200000)
            release = json.loads(payload.decode("utf-8"))
        except (OSError, urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            return
        if not isinstance(release, dict):
            return
        latest_version = str(release.get("tag_name") or release.get("name") or "").strip()
        if not latest_version or not _is_newer_version(latest_version, APP_VERSION):
            return
        download_url = _release_exe_download_url(release)
        self.after(0, lambda: self._show_update_prompt(latest_version, download_url))

    def _show_update_prompt(self, latest_version: str, download_url: str) -> None:
        if not self.winfo_exists():
            return
        dialog = tk.Toplevel(self)
        dialog.title(self.txt("update_title"))
        dialog.transient(self)
        dialog.resizable(False, False)
        dialog.configure(bg="#ffffff")
        dialog.columnconfigure(0, weight=1)

        container = ttk.Frame(dialog, padding=18, style="Chart.TFrame")
        container.grid(row=0, column=0, sticky="nsew")
        container.columnconfigure(0, weight=1)

        title = ttk.Label(container, text=self.txt("update_title"), font=("Microsoft YaHei", 12, "bold"), style="Chart.TLabel")
        title.grid(row=0, column=0, sticky="w", pady=(0, 8))
        message = self.txt("update_message").format(current=APP_VERSION, latest=latest_version.lstrip("v"))
        ttk.Label(container, text=message, justify="left", style="Chart.TLabel").grid(row=1, column=0, sticky="ew")

        buttons = ttk.Frame(container, style="Chart.TFrame")
        buttons.grid(row=2, column=0, sticky="ew", pady=(16, 0))
        buttons.columnconfigure((0, 1), weight=1)

        def open_update() -> None:
            dialog.destroy()
            if _open_url(download_url):
                self.status.set(self.txt("update_opened"))
            else:
                messagebox.showerror(self.txt("title"), self.txt("update_open_failed"), parent=self)

        skip_button = ttk.Button(buttons, text=self.txt("update_skip"), command=dialog.destroy, style="Chart.TButton")
        skip_button.grid(row=0, column=0, sticky="ew", padx=(0, 8))
        update_button = self._primary_button(buttons, command=open_update)
        update_button.configure(text=self.txt("update_now"))
        update_button.grid(row=0, column=1, sticky="ew")

        dialog.protocol("WM_DELETE_WINDOW", dialog.destroy)
        dialog.update_idletasks()
        _center_window(dialog, 420, 210)
        dialog.lift()
        dialog.focus_force()

    def _fill_tree(self, tree: ttk.Treeview, frame: pd.DataFrame) -> None:
        tree.delete(*tree.get_children())
        columns = [str(col) for col in frame.columns]
        tree["columns"] = columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=110, anchor="w")
        for _, row in frame.iterrows():
            tree.insert("", "end", values=[("" if pd.isna(value) else str(value)) for value in row.tolist()])

    def _column_names(self) -> list[str]:
        return [str(col) for col in self.table.columns]

    def _fill_column_combos(self) -> None:
        if not hasattr(self, "category_combo") or not self.category_combo.winfo_exists():
            return
        names = self._column_names()
        self.category_combo.configure(values=names)
        self.value_combo.configure(values=names)
        if names:
            self.category_col.set(names[0])
            self.value_col.set(names[min(1, len(names) - 1)])

    def _fill_asset_list(self) -> None:
        if not hasattr(self, "asset_list") or not self.asset_list.winfo_exists():
            return
        self.asset_list.delete(0, tk.END)
        for name in self._column_names():
            self.asset_list.insert(tk.END, name)
        for index in range(min(3, self.asset_list.size())):
            self.asset_list.selection_set(index)

    def plot(self) -> None:
        if self.raw.empty or self.table.empty:
            messagebox.showwarning(self.txt("title"), self.txt("no_file"))
            return
        if self.mode.get() == "domain" and self.major.get() != "physics":
            self._plot_domain()
        else:
            self._plot_manual()

    def _refresh_plot_if_ready(self) -> None:
        if not self.raw.empty and not self.table.empty:
            self.plot()

    def open_image_params_dialog(self) -> None:
        dialog = tk.Toplevel(self)
        dialog.title(self.txt("image_params"))
        dialog.transient(self)
        dialog.grab_set()
        dialog.resizable(False, False)
        dialog.columnconfigure(1, weight=1)

        fields = [
            (self.txt("plot_title"), self.plot_title),
            (self.txt("x_axis_name"), self.x_axis_name),
            (self.txt("x_unit"), self.x_unit),
            (self.txt("y_axis_name"), self.y_axis_name),
            (self.txt("y_unit"), self.y_unit),
        ]
        for row, (label, variable) in enumerate(fields):
            ttk.Label(dialog, text=label).grid(row=row, column=0, sticky="w", padx=12, pady=(10 if row == 0 else 4, 4))
            ttk.Entry(dialog, textvariable=variable, width=32).grid(row=row, column=1, sticky="ew", padx=12, pady=(10 if row == 0 else 4, 4))

        color_rows = [
            (self.txt("data_color"), self.data_color),
            (self.txt("fit_color"), self.fit_color),
            (self.txt("grid_color"), self.grid_color),
        ]
        start_row = len(fields)
        for offset, (label, variable) in enumerate(color_rows):
            row = start_row + offset
            ttk.Label(dialog, text=label).grid(row=row, column=0, sticky="w", padx=12, pady=4)
            frame = ttk.Frame(dialog)
            frame.grid(row=row, column=1, sticky="ew", padx=12, pady=4)
            frame.columnconfigure(0, weight=1)
            ttk.Entry(frame, textvariable=variable, width=14).grid(row=0, column=0, sticky="ew", padx=(0, 6))
            swatch = tk.Label(frame, text="  ", bg=variable.get(), width=4, relief="solid", borderwidth=1)
            swatch.grid(row=0, column=1, padx=(0, 6))
            ttk.Button(frame, text=self.txt("choose_color"), command=lambda var=variable, box=swatch: self._choose_color(var, box)).grid(row=0, column=2)

        button_frame = ttk.Frame(dialog)
        button_frame.grid(row=start_row + len(color_rows), column=0, columnspan=2, sticky="ew", padx=12, pady=12)
        button_frame.columnconfigure((0, 1), weight=1)
        ttk.Button(button_frame, text=self.txt("cancel"), command=dialog.destroy).grid(row=0, column=0, sticky="ew", padx=(0, 4))

        def apply_and_close() -> None:
            dialog.destroy()
            self._refresh_plot_if_ready()

        ttk.Button(button_frame, text=self.txt("apply"), command=apply_and_close).grid(row=0, column=1, sticky="ew", padx=(4, 0))
        dialog.wait_window()

    def _choose_color(self, variable: StringVar, swatch: tk.Label) -> None:
        _rgb, value = colorchooser.askcolor(color=variable.get(), parent=self)
        if value:
            variable.set(value)
            swatch.configure(bg=value)

    def save_current_plot(self, quiet: bool = False) -> bool:
        if self.current_plot is None:
            if not quiet:
                messagebox.showwarning(self.txt("title"), self.txt("no_current_plot"))
            return False
        self._upsert_current_plot()
        if not quiet:
            self.status.set(f"{self.txt('figure_saved')}: {self.current_plot.name}")
        return True

    def new_figure(self) -> None:
        name = self.txt("default_figure_name").format(number=len(self.saved_plots) + 1)
        placeholder = SavedPlot(
            name=name,
            data=pd.DataFrame(columns=["x", "y"]),
            kind="blank",
            x_label="X",
            y_label="Y",
            title=name,
            sheet=self.sheet.get(),
        )
        self.saved_plots.append(placeholder)
        self.active_plot_index = len(self.saved_plots) - 1
        self.current_plot = placeholder
        self.plot_title.set(name)
        self._reset_xy_range_defaults()
        self._refresh_saved_plots_list()
        self._select_saved_plot(self.active_plot_index)
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_title(name)
        self.canvas.draw()

    def _refresh_saved_plots_list(self) -> None:
        self.saved_plots_list.delete(0, tk.END)
        for index, saved in enumerate(self.saved_plots, start=1):
            marker = "⧉" if saved.kind == "dual_y" else "○" if saved.kind == "blank" else "●"
            self.saved_plots_list.insert(tk.END, f"{index}. {marker} {saved.name}")

    def _select_saved_plot(self, index: int) -> None:
        self.saved_plots_list.selection_clear(0, tk.END)
        self.saved_plots_list.selection_set(index)
        self.saved_plots_list.activate(index)
        self.saved_plots_list.see(index)

    def delete_saved_plot(self, index: int) -> None:
        if index < 0 or index >= len(self.saved_plots):
            return
        deleted_name = self.saved_plots[index].name
        confirmed = messagebox.askyesno(
            self.txt("title"),
            self.txt("confirm_delete_figure").format(name=deleted_name),
        )
        if not confirmed:
            return
        del self.saved_plots[index]
        self.context_plot_index = None
        if not self.saved_plots:
            self.active_plot_index = None
            self.current_plot = None
            self._refresh_saved_plots_list()
            self.new_figure()
            self.status.set(f"{self.txt('figure_deleted')}: {deleted_name}")
            return

        new_index = min(index, len(self.saved_plots) - 1)
        self._refresh_saved_plots_list()
        self._select_saved_plot(new_index)
        self.show_saved_plot(new_index)
        self.status.set(f"{self.txt('figure_deleted')}: {deleted_name}")

    def _copy_plot(self, plot: SavedPlot) -> SavedPlot:
        return SavedPlot(
            name=plot.name,
            data=plot.data.copy(),
            kind=plot.kind,
            x_label=plot.x_label,
            y_label=plot.y_label,
            title=plot.title,
            sheet=plot.sheet,
            parts=plot.parts,
        )

    def _upsert_current_plot(self) -> None:
        if self.current_plot is None:
            return
        saved = self._copy_plot(self.current_plot)
        if self.active_plot_index is None or self.active_plot_index >= len(self.saved_plots):
            self.saved_plots.append(saved)
            self.active_plot_index = len(self.saved_plots) - 1
        else:
            self.saved_plots[self.active_plot_index] = saved
        self._refresh_saved_plots_list()
        self._select_saved_plot(self.active_plot_index)

    def _on_saved_plot_selected(self, _event: object | None = None) -> None:
        selection = list(self.saved_plots_list.curselection())
        if len(selection) != 1:
            return
        self.show_saved_plot(selection[0])

    def show_saved_plot(self, index: int) -> None:
        if index < 0 or index >= len(self.saved_plots):
            return
        saved = self.saved_plots[index]
        self.active_plot_index = index
        if saved.kind == "dual_y" and saved.parts:
            self.draw_dual_y_plot(saved.parts, saved.name)
        elif saved.kind == "blank":
            self.draw_blank_saved_plot(saved)
        else:
            self.draw_single_saved_plot(saved)
        self.current_plot = saved
        self.plot_title.set(saved.title or saved.name)

    def draw_blank_saved_plot(self, saved: SavedPlot) -> None:
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        self._apply_plot_style(ax)
        ax.set_title(saved.title or saved.name)
        ax.set_xlabel(saved.x_label)
        ax.set_ylabel(saved.y_label)
        self.figure.tight_layout()
        self.canvas.draw()

    def draw_single_saved_plot(self, saved: SavedPlot) -> None:
        if saved.kind == "blank" or saved.data.empty:
            self.draw_blank_saved_plot(saved)
            return
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        params = self._style_params()
        self._plot_saved_on_axis(ax, saved, params, self.data_color.get())
        self._apply_plot_style(ax)
        ax.set_xlabel(saved.x_label)
        ax.set_ylabel(saved.y_label)
        ax.set_title(saved.title or saved.name)
        ax.grid(True, color=self.grid_color.get(), alpha=float(params["grid_alpha"]), linestyle=str(params["grid_style"]), linewidth=0.75)
        self._apply_axis_number_format(ax)
        ax.legend(loc="best")
        self.figure.tight_layout()
        self.canvas.draw()

    def combine_selected_plots(self) -> None:
        usable_indices = [index for index, plot in enumerate(self.saved_plots) if plot.kind != "blank"]
        if len(usable_indices) < 2:
            messagebox.showwarning(self.txt("title"), self.txt("select_two_figures"))
            return

        dialog = tk.Toplevel(self)
        dialog.title(self.txt("combine_figures"))
        dialog.transient(self)
        dialog.grab_set()
        dialog.resizable(False, False)
        dialog.columnconfigure(0, weight=1)

        ttk.Label(dialog, text=self.txt("dual_axis_name")).grid(row=0, column=0, sticky="w", padx=12, pady=(12, 2))
        name_var = StringVar(value=self._active_title() or self.txt("combined_title"))
        ttk.Entry(dialog, textvariable=name_var, width=32).grid(row=1, column=0, sticky="ew", padx=12, pady=(0, 10))
        ttk.Label(dialog, text=self.txt("choose_dual_axis_figures")).grid(row=2, column=0, sticky="w", padx=12, pady=(0, 4))

        checks: list[tuple[int, BooleanVar]] = []
        check_frame = ttk.Frame(dialog)
        check_frame.grid(row=3, column=0, sticky="ew", padx=12)
        check_frame.columnconfigure(0, weight=1)
        for row, index in enumerate(usable_indices):
            checked = BooleanVar(value=row < 2)
            checks.append((index, checked))
            ttk.Checkbutton(check_frame, text=f"{index + 1}. {self.saved_plots[index].name}", variable=checked).grid(row=row, column=0, sticky="w", pady=2)

        button_frame = ttk.Frame(dialog)
        button_frame.grid(row=4, column=0, sticky="ew", padx=12, pady=12)
        button_frame.columnconfigure((0, 1), weight=1)
        ttk.Button(button_frame, text=self.txt("cancel"), command=dialog.destroy).grid(row=0, column=0, sticky="ew", padx=(0, 4))

        def confirm() -> None:
            selected_indices = [index for index, checked in checks if checked.get()]
            name = name_var.get().strip() or self.txt("combined_title")
            if self._create_dual_y_plot_from_indices(selected_indices, name):
                dialog.destroy()

        ttk.Button(button_frame, text=self.txt("confirm"), command=confirm).grid(row=0, column=1, sticky="ew", padx=(4, 0))
        dialog.wait_window()

    def _create_dual_y_plot_from_indices(self, selected_indices: list[int], chart_name: str) -> bool:
        selected = [self.saved_plots[index] for index in selected_indices if 0 <= index < len(self.saved_plots) and self.saved_plots[index].kind != "blank"]
        if len(selected) < 2:
            messagebox.showwarning(self.txt("title"), self.txt("select_two_figures"))
            return False
        self.draw_dual_y_plot(selected, chart_name)
        saved = SavedPlot(
            name=chart_name,
            data=selected[0].data.copy(),
            kind="dual_y",
            x_label=selected[0].x_label,
            y_label=selected[0].y_label,
            title=chart_name,
            sheet="",
            parts=[part for part in selected],
        )
        self.current_plot = saved
        self.saved_plots.append(saved)
        self.active_plot_index = len(self.saved_plots) - 1
        self._refresh_saved_plots_list()
        self.saved_plots_list.selection_clear(0, tk.END)
        self._select_saved_plot(self.active_plot_index)
        self.status.set(f"{self.txt('figure_saved')}: {chart_name}")
        return True

    def draw_dual_y_plot(self, selected: list[SavedPlot], title: str) -> None:
        left_plot = selected[0]
        right_plots = selected[1:]
        self.figure.clear()
        ax_left = self.figure.add_subplot(111)
        ax_right = ax_left.twinx()
        params = self._style_params()
        left_color = self.data_color.get()
        right_colors = ["#d62728", "#ff7f0e", "#9467bd", "#2ca02c"]
        self._plot_saved_on_axis(ax_left, left_plot, params, left_color)
        for index, saved in enumerate(right_plots):
            self._plot_saved_on_axis(ax_right, saved, params, right_colors[index % len(right_colors)])

        self._apply_plot_style(ax_left)
        ax_right.set_facecolor("none")
        ax_left.set_xlabel(left_plot.x_label)
        ax_left.set_ylabel(left_plot.y_label, color=left_color)
        right_label = right_plots[0].y_label if len(right_plots) == 1 else self.txt("right_y_axis")
        ax_right.set_ylabel(right_label, color=right_colors[0])
        ax_left.tick_params(axis="y", colors=left_color)
        ax_right.tick_params(axis="y", colors=right_colors[0], labelsize=float(params["font_size"]), width=float(params["spine_width"]))
        ax_left.spines["left"].set_color(left_color)
        ax_right.spines["right"].set_color(right_colors[0])
        ax_left.set_title(title)
        ax_left.grid(True, color=self.grid_color.get(), alpha=float(params["grid_alpha"]), linestyle=str(params["grid_style"]), linewidth=0.75)
        self._apply_axis_number_format(ax_left)
        self._apply_axis_number_format(ax_right)
        left_handles, left_labels = ax_left.get_legend_handles_labels()
        right_handles, right_labels = ax_right.get_legend_handles_labels()
        ax_left.legend(left_handles + right_handles, left_labels + right_labels, loc="best")
        self.figure.tight_layout()
        self.canvas.draw()

    def _plot_saved_on_axis(self, ax: object, saved: SavedPlot, params: dict[str, float | str | bool], color: str) -> None:
        if saved.kind == "scatter":
            ax.scatter(
                saved.data["x"],
                saved.data["y"],
                s=float(params["marker_size"]) ** 2,
                linewidths=float(params["marker_edge_width"]),
                edgecolors=color,
                color=color,
                label=saved.name,
            )
            return
        ax.plot(
            saved.data["x"],
            saved.data["y"],
            marker="o",
            linewidth=float(params["line_width"]),
            markersize=float(params["marker_size"]),
            markeredgewidth=float(params["marker_edge_width"]),
            color=color,
            label=saved.name,
        )

    def analyze_current_xy_data(self) -> None:
        if self.mode.get() != "manual":
            messagebox.showwarning(self.txt("title"), self.txt("analysis_need_xy"))
            return
        data = self._xy_frame()
        if len(data) < 2:
            messagebox.showwarning(self.txt("title"), self.txt("analysis_need_xy"))
            return

        self._open_analysis_dialog(data)

    def _open_analysis_dialog(self, data: pd.DataFrame) -> None:
        dialog = tk.Toplevel(self)
        dialog.title(self.txt("analysis_result"))
        dialog.transient(self)
        dialog.grab_set()
        dialog.columnconfigure(1, weight=1)
        dialog.rowconfigure(4, weight=1)

        x_min_var = DoubleVar(value=float(data["x"].min()))
        x_max_var = DoubleVar(value=float(data["x"].max()))
        result_state: dict[str, object] = {}

        ttk.Label(dialog, text=self.txt("analysis_x_min")).grid(row=0, column=0, sticky="w", padx=12, pady=(12, 4))
        ttk.Entry(dialog, textvariable=x_min_var, width=18).grid(row=0, column=1, sticky="ew", padx=12, pady=(12, 4))
        ttk.Label(dialog, text=self.txt("analysis_x_max")).grid(row=1, column=0, sticky="w", padx=12, pady=4)
        ttk.Entry(dialog, textvariable=x_max_var, width=18).grid(row=1, column=1, sticky="ew", padx=12, pady=4)

        add_line = BooleanVar(value=True)
        show_equation = BooleanVar(value=True)
        show_slope_intercept = BooleanVar(value=True)
        show_correlation = BooleanVar(value=True)

        options = ttk.Frame(dialog)
        options.grid(row=2, column=0, columnspan=2, sticky="ew", padx=12, pady=(6, 2))
        ttk.Checkbutton(options, text=self.txt("add_regression_line"), variable=add_line).grid(row=0, column=0, sticky="w")
        ttk.Checkbutton(options, text=self.txt("show_equation_on_chart"), variable=show_equation).grid(row=1, column=0, sticky="w")
        ttk.Checkbutton(options, text=self.txt("show_slope_intercept_on_chart"), variable=show_slope_intercept).grid(row=2, column=0, sticky="w")
        ttk.Checkbutton(options, text=self.txt("show_correlation_on_chart"), variable=show_correlation).grid(row=3, column=0, sticky="w")

        result_text = tk.Text(dialog, width=58, height=10, wrap="word")
        result_text.grid(row=4, column=0, columnspan=2, sticky="nsew", padx=12, pady=8)

        def set_result_text(text: str) -> None:
            result_text.configure(state="normal")
            result_text.delete("1.0", tk.END)
            result_text.insert("1.0", text)
            result_text.configure(state="disabled")

        def calculate() -> None:
            subset = self._analysis_subset(data, x_min_var.get(), x_max_var.get())
            if len(subset) < 2:
                messagebox.showwarning(self.txt("title"), self.txt("analysis_need_xy"))
                return
            result = self._linear_regression_analysis(subset)
            lines = self._format_analysis_lines(result)
            result_state["subset"] = subset
            result_state["result"] = result
            result_state["lines"] = lines
            set_result_text("\n".join(lines))

        def apply_to_chart() -> None:
            if "result" not in result_state:
                calculate()
            if "result" not in result_state:
                return
            self._apply_analysis_to_chart(
                result_state["subset"],
                result_state["result"],
                add_line=add_line.get(),
                show_equation=show_equation.get(),
                show_slope_intercept=show_slope_intercept.get(),
                show_correlation=show_correlation.get(),
            )
            dialog.destroy()

        button_frame = ttk.Frame(dialog)
        button_frame.grid(row=5, column=0, columnspan=2, sticky="ew", padx=12, pady=(0, 12))
        button_frame.columnconfigure((0, 1, 2), weight=1)
        ttk.Button(button_frame, text=self.txt("calculate"), command=calculate).grid(row=0, column=0, sticky="ew", padx=(0, 4))
        ttk.Button(button_frame, text=self.txt("apply_to_chart"), command=apply_to_chart).grid(row=0, column=1, sticky="ew", padx=4)
        ttk.Button(button_frame, text=self.txt("cancel"), command=dialog.destroy).grid(row=0, column=2, sticky="ew", padx=(4, 0))

        calculate()
        dialog.wait_window()

    def _analysis_subset(self, data: pd.DataFrame, x_min: float, x_max: float) -> pd.DataFrame:
        lo, hi = sorted((x_min, x_max))
        subset = data[(data["x"] >= lo) & (data["x"] <= hi)].copy()
        return subset.reset_index(drop=True)

    def _format_analysis_lines(self, result: dict[str, float]) -> list[str]:
        return [
            f"{self.txt('regression_equation')}: y = {result['slope']:.6g}x + {result['intercept']:.6g}",
            f"{self.txt('slope_value')}: {result['slope']:.6g}",
            f"{self.txt('intercept')}: {result['intercept']:.6g}",
            f"{self.txt('correlation_r')}: {result['r']:.6g}",
            f"{self.txt('determination_r2')}: {result['r2']:.6g}",
            f"{self.txt('rmse')}: {result['rmse']:.6g}",
            f"{self.txt('sample_count')}: {int(result['n'])}",
        ]

    def _apply_analysis_to_chart(
        self,
        subset: pd.DataFrame,
        result: dict[str, float],
        add_line: bool,
        show_equation: bool,
        show_slope_intercept: bool,
        show_correlation: bool,
    ) -> None:
        self._plot_manual()
        if not self.figure.axes:
            return
        ax = self.figure.axes[0]
        if add_line:
            xs = np.linspace(subset["x"].min(), subset["x"].max(), 100)
            ys = result["slope"] * xs + result["intercept"]
            ax.plot(xs, ys, "--", linewidth=float(self._style_params()["fit_width"]), color=self.fit_color.get(), label=self.txt("fit"))
            ax.legend(loc="best")

        annotation_lines: list[str] = []
        if show_equation:
            annotation_lines.append(f"y = {result['slope']:.6g}x + {result['intercept']:.6g}")
        if show_slope_intercept:
            annotation_lines.append(f"{self.txt('slope_value')}: {result['slope']:.6g}")
            annotation_lines.append(f"{self.txt('intercept')}: {result['intercept']:.6g}")
        if show_correlation:
            annotation_lines.append(f"{self.txt('correlation_r')}: {result['r']:.6g}")
            annotation_lines.append(f"{self.txt('determination_r2')}: {result['r2']:.6g}")
        if annotation_lines:
            ax.text(
                0.02,
                0.98,
                "\n".join(annotation_lines),
                transform=ax.transAxes,
                va="top",
                ha="left",
                fontsize=9,
                bbox=dict(boxstyle="round", facecolor="white", edgecolor="#444444", alpha=0.88),
            )
        summary = self._format_analysis_lines(result)
        self.status.set(" | ".join(summary[:5]))
        self.figure.tight_layout()
        self.canvas.draw()

    def _linear_regression_analysis(self, data: pd.DataFrame) -> dict[str, float]:
        x = data["x"].astype(float).to_numpy()
        y = data["y"].astype(float).to_numpy()
        slope, intercept = np.polyfit(x, y, 1)
        predicted = slope * x + intercept
        residuals = y - predicted
        ss_res = float(np.sum(residuals**2))
        ss_tot = float(np.sum((y - np.mean(y)) ** 2))
        r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
        r = float(np.corrcoef(x, y)[0, 1]) if np.std(x) > 0 and np.std(y) > 0 else float("nan")
        rmse = float(np.sqrt(np.mean(residuals**2)))
        return {
            "slope": float(slope),
            "intercept": float(intercept),
            "r": r,
            "r2": float(r2),
            "rmse": rmse,
            "n": float(len(data)),
        }

    def _show_analysis_dialog(self, result_text: str) -> None:
        dialog = tk.Toplevel(self)
        dialog.title(self.txt("analysis_result"))
        dialog.transient(self)
        dialog.grab_set()
        dialog.columnconfigure(0, weight=1)
        dialog.rowconfigure(0, weight=1)
        text = tk.Text(dialog, width=52, height=10, wrap="word")
        text.grid(row=0, column=0, sticky="nsew", padx=12, pady=12)
        text.insert("1.0", result_text)
        text.configure(state="disabled")
        ttk.Button(dialog, text=self.txt("confirm"), command=dialog.destroy).grid(row=1, column=0, sticky="ew", padx=12, pady=(0, 12))
        dialog.wait_window()

    def _extract(self, controls: RangeControls) -> pd.Series:
        row_count = len(self.raw)
        col_count = len(self.raw.columns)
        sr = max(1, min(controls.start_row.get(), row_count))
        er = max(1, min(controls.end_row.get(), row_count))
        sc = max(1, min(controls.start_col.get(), col_count))
        ec = max(1, min(controls.end_col.get(), col_count))
        if controls.orientation.get() == "horizontal":
            block = self.raw.iloc[sr - 1 : sr, min(sc, ec) - 1 : max(sc, ec)]
        else:
            block = self.raw.iloc[min(sr, er) - 1 : max(sr, er), sc - 1 : sc]
        values = block.to_numpy().reshape(-1)
        return pd.to_numeric(pd.Series(values), errors="coerce").dropna().reset_index(drop=True)

    def _xy_frame(self) -> pd.DataFrame:
        x = self._extract(self.x_range)
        y = self._extract(self.y_range)
        length = min(len(x), len(y))
        return pd.DataFrame({"x": x.iloc[:length], "y": y.iloc[:length]}).dropna().reset_index(drop=True)

    def _axis_labels(self, kind: str) -> tuple[str, str]:
        x_name = self.x_axis_name.get().strip() or "X"
        y_name = self.y_axis_name.get().strip() or "Y"
        x_label = x_name + (f" ({self.x_unit.get()})" if self.x_unit.get() else "")
        y_label = y_name + (f" ({self.y_unit.get()})" if self.y_unit.get() else "")
        if kind == "hist":
            return y_label, "Count"
        return x_label, y_label

    def _active_title(self) -> str:
        return self.plot_title.get().strip()

    def _apply_title(self, ax: object) -> None:
        title = self._active_title()
        if title:
            ax.set_title(title)

    def _style_params(self) -> dict[str, float | str | bool]:
        if self.plot_style.get() == "presentation":
            return {
                "line_width": 2.2,
                "fit_width": 2.0,
                "marker_size": 6.5,
                "marker_edge_width": 0.6,
                "bar_alpha": 0.86,
                "grid_alpha": 0.25,
                "grid_style": "-",
                "spine_width": 1.0,
                "font_size": 11,
            }
        return {
            "line_width": 1.15,
            "fit_width": 1.35,
            "marker_size": 4.2,
            "marker_edge_width": 0.75,
            "bar_alpha": 0.78,
            "grid_alpha": 0.28,
            "grid_style": "--",
            "spine_width": 0.8,
            "font_size": 10,
        }

    def _apply_axis_number_format(self, ax: object) -> None:
        x_formatter = ScalarFormatter(useMathText=True, useOffset=False)
        x_formatter.set_scientific(self.scientific_x.get())
        x_formatter.set_powerlimits((0, 0) if self.scientific_x.get() else (-6, 6))
        y_formatter = ScalarFormatter(useMathText=True, useOffset=False)
        y_formatter.set_scientific(self.scientific_y.get())
        y_formatter.set_powerlimits((0, 0) if self.scientific_y.get() else (-6, 6))
        ax.xaxis.set_major_formatter(x_formatter)
        ax.yaxis.set_major_formatter(y_formatter)

    def _apply_plot_style(self, ax: object) -> None:
        params = self._style_params()
        ax.set_facecolor("white")
        self.figure.patch.set_facecolor("white")
        for spine in ax.spines.values():
            spine.set_linewidth(float(params["spine_width"]))
            spine.set_color("#111111")
        ax.tick_params(axis="both", labelsize=float(params["font_size"]), width=float(params["spine_width"]))

    def _plot_manual(self) -> None:
        data = self._xy_frame()
        if len(data) < 2:
            messagebox.showwarning(self.txt("title"), self.txt("not_enough"))
            return
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        params = self._style_params()
        kind = self.chart_kind.get()
        yerr = None
        if self.use_error.get():
            err = self._extract(self.err_range)
            if len(err) >= len(data):
                yerr = err.iloc[: len(data)]

        if kind == "line":
            ax.errorbar(
                data["x"],
                data["y"],
                yerr=yerr,
                color=self.data_color.get(),
                marker="o",
                linewidth=float(params["line_width"]),
                markersize=float(params["marker_size"]),
                markeredgewidth=float(params["marker_edge_width"]),
                markeredgecolor="white" if self.plot_style.get() == "presentation" else self.data_color.get(),
                capsize=2.5,
            )
        elif kind == "bar":
            ax.bar(data["x"], data["y"], yerr=yerr, color=self.data_color.get(), alpha=float(params["bar_alpha"]), linewidth=0.8, edgecolor="#222222")
        elif kind == "hist":
            ax.hist(data["y"], bins="auto", color=self.data_color.get(), alpha=float(params["bar_alpha"]), linewidth=0.8, edgecolor="#222222")
        else:
            ax.errorbar(
                data["x"],
                data["y"],
                yerr=yerr,
                fmt="o",
                color=self.data_color.get(),
                markersize=float(params["marker_size"]),
                markeredgewidth=float(params["marker_edge_width"]),
                markeredgecolor=self.data_color.get(),
                capsize=2.5,
            )

        result_lines: list[str] = []
        self._add_fit(ax, data, result_lines)
        self._add_slope(data, result_lines)
        self._style_axes(ax, kind)
        x_label, y_label = self._axis_labels(kind)
        if self._active_title():
            default_name = self._active_title()
        elif self.active_plot_index is not None and self.active_plot_index < len(self.saved_plots):
            default_name = self.saved_plots[self.active_plot_index].name
        else:
            default_name = self.txt("default_figure_name").format(number=len(self.saved_plots) + 1)
        self.current_plot = SavedPlot(
            name=default_name,
            data=data.copy(),
            kind=kind,
            x_label=x_label,
            y_label=y_label,
            title=self._active_title() or default_name,
            sheet=self.sheet.get(),
        )
        self._upsert_current_plot()
        self.figure.tight_layout()
        self.canvas.draw()
        self.status.set(" | ".join(result_lines) if result_lines else self.txt("status_ready"))

    def _add_fit(self, ax: object, data: pd.DataFrame, result_lines: list[str]) -> None:
        kind = self.fit_kind.get()
        if kind == "none":
            return
        degree = 1 if kind == "linear" else 2
        if len(data) < degree + 1:
            return
        coeffs = np.polyfit(data["x"], data["y"], degree)
        xs = np.linspace(data["x"].min(), data["x"].max(), 120)
        ys = np.polyval(coeffs, xs)
        params = self._style_params()
        ax.plot(xs, ys, "--", linewidth=float(params["fit_width"]), color=self.fit_color.get(), label=self.txt("fit"))
        ax.legend()
        if degree == 1:
            result_lines.append(f"{self.txt('fit_result')}: y = {coeffs[0]:.6g}x + {coeffs[1]:.6g}")
        else:
            result_lines.append(f"{self.txt('fit_result')}: y = {coeffs[0]:.6g}x² + {coeffs[1]:.6g}x + {coeffs[2]:.6g}")

    def _add_slope(self, data: pd.DataFrame, result_lines: list[str]) -> None:
        if not self.use_slope.get() or len(data) < 2:
            return
        lo = max(1, min(self.slope_start.get(), len(data)))
        hi = max(1, min(self.slope_end.get(), len(data)))
        subset = data.iloc[min(lo, hi) - 1 : max(lo, hi)]
        if len(subset) < 2:
            return
        slope = np.polyfit(subset["x"], subset["y"], 1)[0]
        result_lines.append(f"{self.txt('slope_value')}: {slope:.6g}")

    def _style_axes(self, ax: object, kind: str) -> None:
        self._apply_plot_style(ax)
        if self.show_axes.get():
            params = self._style_params()
            x_label, y_label = self._axis_labels(kind)
            ax.set_xlabel(x_label)
            ax.set_ylabel(y_label)
            ax.grid(True, color=self.grid_color.get(), alpha=float(params["grid_alpha"]), linestyle=str(params["grid_style"]), linewidth=0.75)
            self._apply_axis_number_format(ax)
            self._apply_title(ax)
        else:
            ax.axis("off")

    def _plot_domain(self) -> None:
        self.current_plot = None
        self.active_plot_index = None
        if self.major.get() == "finance":
            self._plot_finance()
        else:
            self._plot_accounting()

    def _plot_accounting(self) -> None:
        category = self.category_col.get()
        value = self.value_col.get()
        if not category or not value:
            messagebox.showwarning(self.txt("title"), self.txt("not_enough"))
            return
        frame = pd.DataFrame(
            {
                "category": self.table[category].astype(str),
                "value": pd.to_numeric(self.table[value], errors="coerce"),
            }
        ).dropna()
        if frame.empty:
            messagebox.showwarning(self.txt("title"), self.txt("not_enough"))
            return
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        params = self._style_params()
        chart = self.domain_chart.get()
        if chart == "pie":
            ax.pie(frame["value"].abs(), labels=frame["category"], autopct="%1.1f%%")
        elif chart == "waterfall":
            running = frame["value"].cumsum() - frame["value"]
            colors = ["#2ca02c" if value >= 0 else "#d62728" for value in frame["value"]]
            ax.bar(frame["category"], frame["value"], bottom=running, color=colors, alpha=float(params["bar_alpha"]), linewidth=0.8, edgecolor="#222222")
            ax.plot(
                frame["category"],
                frame["value"].cumsum(),
                color="#333333",
                marker="o",
                linewidth=float(params["line_width"]),
                markersize=float(params["marker_size"]),
            )
            ax.axhline(0, color="#333333", linewidth=0.8)
        elif chart == "line":
            ax.plot(
                frame["category"],
                frame["value"],
                marker="o",
                linewidth=float(params["line_width"]),
                markersize=float(params["marker_size"]),
            )
        else:
            ax.bar(frame["category"], frame["value"], alpha=float(params["bar_alpha"]), linewidth=0.8, edgecolor="#222222")
        ax.tick_params(axis="x", rotation=25)
        self._apply_plot_style(ax)
        ax.grid(True, axis="y", color=self.grid_color.get(), alpha=float(params["grid_alpha"]), linestyle=str(params["grid_style"]), linewidth=0.75)
        self._apply_axis_number_format(ax)
        self._apply_title(ax)
        self.figure.tight_layout()
        self.canvas.draw()

    def _plot_finance(self) -> None:
        selected = [self.asset_list.get(index) for index in self.asset_list.curselection()]
        if not selected:
            messagebox.showwarning(self.txt("title"), self.txt("select_assets"))
            return
        data = self.table[selected].apply(pd.to_numeric, errors="coerce").dropna(how="all")
        if data.empty:
            messagebox.showwarning(self.txt("title"), self.txt("not_enough"))
            return
        returns = data.pct_change(fill_method=None).replace([np.inf, -np.inf], np.nan).dropna(how="all")

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        params = self._style_params()
        chart = self.domain_chart.get()
        if chart == "portfolio":
            weights = np.ones(len(selected)) / len(selected)
            ax.pie(weights, labels=selected, autopct="%1.1f%%")
            self._apply_title(ax)
        elif chart == "cumulative":
            if returns.empty:
                messagebox.showwarning(self.txt("title"), self.txt("not_enough"))
                return
            cumulative = (1 + returns.fillna(0)).cumprod() - 1
            cumulative.plot(ax=ax, linewidth=float(params["line_width"]), marker="o", markersize=float(params["marker_size"]))
            ax.set_ylabel("Return")
            self._apply_plot_style(ax)
            ax.grid(True, color=self.grid_color.get(), alpha=float(params["grid_alpha"]), linestyle=str(params["grid_style"]), linewidth=0.75)
            self._apply_axis_number_format(ax)
            self._apply_title(ax)
        elif chart == "corr":
            if returns.empty:
                messagebox.showwarning(self.txt("title"), self.txt("not_enough"))
                return
            corr = returns.corr()
            image = ax.imshow(corr, vmin=-1, vmax=1, cmap="coolwarm")
            ax.set_xticks(range(len(corr.columns)), corr.columns, rotation=35, ha="right")
            ax.set_yticks(range(len(corr.index)), corr.index)
            self.figure.colorbar(image, ax=ax)
            for i in range(len(corr.index)):
                for j in range(len(corr.columns)):
                    ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center", color="white" if abs(corr.iloc[i, j]) > 0.5 else "black")
            self._apply_title(ax)
        else:
            if returns.empty:
                messagebox.showwarning(self.txt("title"), self.txt("not_enough"))
                return
            risk = returns.std()
            reward = returns.mean()
            marker_area = float(params["marker_size"]) ** 2 * (2.2 if self.plot_style.get() == "presentation" else 1.6)
            ax.scatter(risk, reward, s=marker_area, linewidths=float(params["marker_edge_width"]), edgecolors="#1f77b4")
            for name in selected:
                if name in risk.index and not math.isnan(risk[name]) and not math.isnan(reward[name]):
                    ax.annotate(name, (risk[name], reward[name]), xytext=(5, 5), textcoords="offset points")
            ax.set_xlabel(self.txt("risk"))
            ax.set_ylabel(self.txt("fit_result"))
            self._apply_plot_style(ax)
            ax.grid(True, color=self.grid_color.get(), alpha=float(params["grid_alpha"]), linestyle=str(params["grid_style"]), linewidth=0.75)
            self._apply_axis_number_format(ax)
            self._apply_title(ax)

        self.figure.tight_layout()
        self.canvas.draw()


def main() -> None:
    try:
        import pyi_splash  # type: ignore[import-not-found]

        pyi_splash.update_text("Starting UniGraph...")
        pyi_splash.close()
    except Exception:
        pass
    language = _run_startup_dialog(_load_saved_language())
    app = UniGraphDesktop(initial_language=language)
    app.mainloop()


if __name__ == "__main__":
    main()
