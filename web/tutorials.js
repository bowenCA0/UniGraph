const tutorialTranslations = {
  en: {
    pageTitle: "UniGraph Tutorials - Chart guides by Bowen",
    metaDescription:
      "UniGraph tutorials by Bowen, covering scatter, line, bar, histogram, pie, waterfall, finance, dual-axis, and regression analysis charts.",
    brandAria: "Back to UniGraph home",
    navAria: "Tutorial navigation",
    backHome: "Home",
    download: "Download",
    support: "Support",
    languageLabel: "Language",
    heroEyebrow: "Tutorials",
    heroTitle: "UniGraph chart tutorials",
    heroText:
      "Step-by-step guides for every chart type in UniGraph, written for students who want clean academic figures without fighting code first.",
    authorLabel: "Author standard",
    quickEyebrow: "Quick start",
    quick1: "Import an Excel or CSV file.",
    quick2: "Choose your major and chart type.",
    quick3: "Select X/Y data ranges vertically or horizontally.",
    quick4: "Adjust image parameters, then create the chart.",
    tocAria: "Tutorial categories",
    tocScatter: "Scatter",
    tocLine: "Line",
    tocBar: "Bar",
    tocHist: "Histogram",
    tocPie: "Pie",
    tocWaterfall: "Waterfall",
    tocRisk: "Risk-return",
    tocPortfolio: "Portfolio",
    tocCumulative: "Cumulative",
    tocCorr: "Heatmap",
    tocDual: "Dual Y-axis",
    tocAnalysis: "Analysis",
    footerAuthor: "Tutorial author standard: Bowen",
    scatterTitle: "Scatter plot",
    scatterUse: "Best for lab measurements where every point is an observed X/Y pair.",
    scatterStep1: "Choose Manual X/Y plot and select Scatter.",
    scatterStep2: "Set X and Y ranges; vertical mode means one column plus start/end rows.",
    scatterStep3: "Open Image parameters to name axes, units, colors, and title.",
    scatterStep4: "Enable fit or one-click analysis when you need regression results.",
    scatterTip: "Tip: For physics reports, keep academic style and add error bars when uncertainty is available.",
    lineTitle: "Line chart",
    lineUse: "Best for trends over time, current, voltage, or any ordered variable.",
    lineStep1: "Select Line after importing your data.",
    lineStep2: "Make sure X values are ordered from small to large or in time order.",
    lineStep3: "Use academic style for thin lines and clearer points.",
    lineStep4: "Switch to scientific notation if tick labels are too long.",
    lineTip: "Tip: Use line charts for continuous trends, not unrelated categories.",
    barTitle: "Bar chart",
    barUse: "Best for comparing categories such as expenses, departments, or experiment groups.",
    barStep1: "Use Accounting visuals or Manual X/Y plot, then select Bar.",
    barStep2: "Choose a category column and a numeric value column.",
    barStep3: "Keep labels short; rotate labels if categories are long.",
    barStep4: "Use title and units to make the meaning explicit.",
    barTip: "Tip: Sort values before import if you want a ranked bar chart.",
    histTitle: "Histogram",
    histUse: "Best for seeing the distribution of one numeric variable.",
    histStep1: "Select Histogram and choose the numeric data range.",
    histStep2: "Use one variable only; categories should not be used here.",
    histStep3: "Check whether the distribution is centered, skewed, or has outliers.",
    histStep4: "Add a clear title describing the sample.",
    histTip: "Tip: Histograms explain spread; bar charts compare categories.",
    pieTitle: "Pie chart",
    pieUse: "Best for showing composition, such as expense shares or portfolio weights.",
    pieStep1: "Choose Accounting visuals and select Pie chart.",
    pieStep2: "Set the category column and value column.",
    pieStep3: "Use positive values only and avoid too many slices.",
    pieStep4: "If there are many small items, group them before import.",
    pieTip: "Tip: Pie charts work best for 3 to 6 categories.",
    waterfallTitle: "Cash-flow waterfall",
    waterfallUse: "Best for explaining how inflows and outflows build a final result.",
    waterfallStep1: "Choose Accounting visuals and select Cash-flow waterfall.",
    waterfallStep2: "Use one column for labels and one column for signed amounts.",
    waterfallStep3: "Positive values increase the total; negative values decrease it.",
    waterfallStep4: "Use a title such as Monthly cash movement or Budget bridge.",
    waterfallTip: "Tip: Waterfall charts are more explanatory than ordinary bars for financial movement.",
    riskTitle: "Risk-return chart",
    riskUse: "Best for comparing assets by volatility and average return.",
    riskStep1: "Choose Finance and select Risk-return chart.",
    riskStep2: "Select at least two asset price or value columns.",
    riskStep3: "UniGraph calculates returns, standard deviation, and mean return.",
    riskStep4: "Read rightward as higher risk and upward as higher reward.",
    riskTip: "Tip: Use consistent date intervals for all assets.",
    portfolioTitle: "Portfolio chart",
    portfolioUse: "Best for showing how selected assets are allocated in a simple portfolio.",
    portfolioStep1: "Choose Finance and select Portfolio chart.",
    portfolioStep2: "Select the asset columns you want to include.",
    portfolioStep3: "Use clear asset names in your spreadsheet headers.",
    portfolioStep4: "Use the chart as a visual summary, not as investment advice.",
    portfolioTip: "Tip: Keep asset names short so labels remain readable.",
    cumulativeTitle: "Cumulative return chart",
    cumulativeUse: "Best for comparing asset growth paths over time.",
    cumulativeStep1: "Choose Finance and select Cumulative returns.",
    cumulativeStep2: "Select asset columns with aligned dates or periods.",
    cumulativeStep3: "Use the legend to compare growth paths.",
    cumulativeStep4: "Check sudden jumps for missing or abnormal data.",
    cumulativeTip: "Tip: Clean missing values before comparing multiple assets.",
    corrTitle: "Correlation heatmap",
    corrUse: "Best for seeing whether assets move together or independently.",
    corrStep1: "Choose Finance and select Correlation heatmap.",
    corrStep2: "Select multiple asset columns.",
    corrStep3: "Read values close to 1 as strong positive movement together.",
    corrStep4: "Read values close to 0 as weaker relationship.",
    corrTip: "Tip: Correlation is useful, but it does not prove causation.",
    dualTitle: "Dual Y-axis chart",
    dualUse: "Best for combining two saved charts with different Y units.",
    dualStep1: "Create the first chart and keep it in the right figure manager.",
    dualStep2: "Click New figure and create the second chart.",
    dualStep3: "Click Dual Y-axis chart and choose the figures to combine.",
    dualStep4: "Name the combined chart and verify both axes are labeled.",
    dualTip: "Tip: Use dual axes only when the two variables share the same X meaning.",
    analysisTitle: "One-click data analysis",
    analysisUse: "Best for experiment reports that need slope, intercept, regression equation, r, and R².",
    analysisStep1: "Create a manual X/Y chart first.",
    analysisStep2: "Click One-click analysis in the left panel.",
    analysisStep3: "Select the X range used for the regression.",
    analysisStep4: "Choose which results to add back onto the chart.",
    analysisTip: "Tip: Report both the equation and R² when explaining a linear relationship.",
  },
  zh: {
    pageTitle: "UniGraph 教程 - Bowen 编写的图形指南",
    metaDescription: "Bowen 编写的 UniGraph 教程，覆盖散点图、折线图、柱状图、直方图、饼图、瀑布图、金融图、双 Y 轴和回归分析。",
    brandAria: "返回 UniGraph 首页",
    navAria: "教程页面导航",
    backHome: "首页",
    download: "下载",
    support: "支持",
    languageLabel: "语言",
    heroEyebrow: "教程",
    heroTitle: "UniGraph 图形教程",
    heroText: "这里按图形类型整理 UniGraph 的操作教程，面向想快速做出清晰学术图形、但不想先被代码门槛拦住的学生。",
    authorLabel: "作者标准",
    quickEyebrow: "快速开始",
    quick1: "导入 Excel 或 CSV 文件。",
    quick2: "选择专业和图形类型。",
    quick3: "按竖向或横向选择 X/Y 数据范围。",
    quick4: "设置图像参数，然后生成图表。",
    tocAria: "教程分类",
    tocScatter: "散点图",
    tocLine: "折线图",
    tocBar: "柱状图",
    tocHist: "直方图",
    tocPie: "饼图",
    tocWaterfall: "瀑布图",
    tocRisk: "风险收益",
    tocPortfolio: "资产组合",
    tocCumulative: "累计收益",
    tocCorr: "热力图",
    tocDual: "双 Y 轴",
    tocAnalysis: "数据分析",
    footerAuthor: "教程作者标准：Bowen",
    scatterTitle: "散点图",
    scatterUse: "适合物理实验测量数据，每一个点都是一组真实观测的 X/Y 数据。",
    scatterStep1: "选择“手动 X/Y 绘图”，图表选择“散点图”。",
    scatterStep2: "设置 X 和 Y 范围；竖向表示选择一列，再设置开始行和结束行。",
    scatterStep3: "打开“图像参数设置”，填写坐标轴名称、单位、颜色和标题。",
    scatterStep4: "需要回归结果时，开启拟合或点击一键数据分析。",
    scatterTip: "提示：物理实验报告建议使用学术模式；有不确定度时加入误差棒。",
    lineTitle: "折线图",
    lineUse: "适合展示随时间、电流、电压或其他有顺序变量变化的趋势。",
    lineStep1: "导入数据后选择“折线图”。",
    lineStep2: "确认 X 值按从小到大或时间顺序排列。",
    lineStep3: "使用学术模式获得更细的线条和更清晰的点。",
    lineStep4: "刻度文字太长时，开启科学计数法。",
    lineTip: "提示：折线图适合连续趋势，不适合互不相关的分类。",
    barTitle: "柱状图",
    barUse: "适合比较支出、部门、实验组等分类数据。",
    barStep1: "使用会计可视化或手动 X/Y 绘图，然后选择柱状图。",
    barStep2: "选择分类列和数值列。",
    barStep3: "分类名称尽量简短；名称较长时让标签旋转显示。",
    barStep4: "通过标题和单位说明图形含义。",
    barTip: "提示：如果想做排名图，先在表格里排序再导入。",
    histTitle: "直方图",
    histUse: "适合观察一个数值变量的分布情况。",
    histStep1: "选择直方图，并选择一段数值数据范围。",
    histStep2: "只使用一个变量；分类名称不适合放入直方图。",
    histStep3: "观察数据是否集中、偏斜或存在异常值。",
    histStep4: "添加能说明样本来源的标题。",
    histTip: "提示：直方图解释分布，柱状图比较分类。",
    pieTitle: "饼图",
    pieUse: "适合展示构成比例，例如费用占比或资产权重。",
    pieStep1: "选择会计可视化，再选择饼图。",
    pieStep2: "设置类别列和金额列。",
    pieStep3: "尽量使用正数，避免切片过多。",
    pieStep4: "如果小项目太多，建议先在表格中合并为“其他”。",
    pieTip: "提示：饼图最适合 3 到 6 个类别。",
    waterfallTitle: "现金流瀑布图",
    waterfallUse: "适合解释收入、支出如何一步步形成最终结果。",
    waterfallStep1: "选择会计可视化，再选择现金流瀑布图。",
    waterfallStep2: "使用一列标签和一列带正负号的金额。",
    waterfallStep3: "正数表示增加，负数表示减少。",
    waterfallStep4: "标题可写成“月度现金流变化”或“预算桥接”。",
    waterfallTip: "提示：瀑布图比普通柱状图更适合解释财务变化过程。",
    riskTitle: "风险-收益图",
    riskUse: "适合用波动率和平均收益比较不同资产。",
    riskStep1: "选择金融专业，再选择风险-收益图。",
    riskStep2: "至少选择两列资产价格或价值数据。",
    riskStep3: "UniGraph 会计算收益率、标准差和平均收益。",
    riskStep4: "越往右表示风险越高，越往上表示平均收益越高。",
    riskTip: "提示：所有资产要使用一致的日期或周期。",
    portfolioTitle: "资产组合图",
    portfolioUse: "适合展示所选资产在简单组合中的占比。",
    portfolioStep1: "选择金融专业，再选择资产组合图。",
    portfolioStep2: "选择需要纳入组合的资产列。",
    portfolioStep3: "表格列名建议直接使用清晰的资产名称。",
    portfolioStep4: "该图用于学习和展示，不构成投资建议。",
    portfolioTip: "提示：资产名称越短，图中标签越清楚。",
    cumulativeTitle: "累计收益图",
    cumulativeUse: "适合比较不同资产随时间增长的路径。",
    cumulativeStep1: "选择金融专业，再选择累计收益图。",
    cumulativeStep2: "选择日期或周期对齐的资产列。",
    cumulativeStep3: "通过图例比较不同资产的增长曲线。",
    cumulativeStep4: "如果出现突然跳变，检查是否有缺失或异常数据。",
    cumulativeTip: "提示：比较多个资产前，先清理缺失值。",
    corrTitle: "相关性热力图",
    corrUse: "适合观察资产之间是否同向变化或相对独立。",
    corrStep1: "选择金融专业，再选择相关性热力图。",
    corrStep2: "选择多个资产列。",
    corrStep3: "接近 1 表示强正相关。",
    corrStep4: "接近 0 表示关系较弱。",
    corrTip: "提示：相关性有用，但不能证明因果关系。",
    dualTitle: "双 Y 轴图",
    dualUse: "适合合并两个 Y 单位不同但 X 含义相同的已保存图形。",
    dualStep1: "先生成第一张图，并在右侧图形管理中保留。",
    dualStep2: "点击新建图形，生成第二张图。",
    dualStep3: "点击生成双 Y 轴图，勾选要合并的图形。",
    dualStep4: "命名双 Y 轴图，并确认两个 Y 轴标签都清楚。",
    dualTip: "提示：只有两个变量共享同一个 X 含义时才建议使用双 Y 轴。",
    analysisTitle: "一键数据分析",
    analysisUse: "适合需要斜率、截距、线性回归方程、r 和 R² 的实验报告。",
    analysisStep1: "先生成一张手动 X/Y 图。",
    analysisStep2: "在左侧面板点击一键数据分析。",
    analysisStep3: "选择用于回归的 X 轴范围。",
    analysisStep4: "勾选需要添加回原图的结果。",
    analysisTip: "提示：解释线性关系时，建议同时报告方程和 R²。",
  },
  fr: {
    pageTitle: "Tutoriels UniGraph - Guides de graphiques par Bowen",
    metaDescription:
      "Tutoriels UniGraph par Bowen : nuage de points, courbe, barres, histogramme, camembert, cascade, finance, double axe Y et analyse de régression.",
    brandAria: "Retour à l'accueil UniGraph",
    navAria: "Navigation des tutoriels",
    backHome: "Accueil",
    download: "Télécharger",
    support: "Soutenir",
    languageLabel: "Langue",
    heroEyebrow: "Tutoriels",
    heroTitle: "Tutoriels de graphiques UniGraph",
    heroText:
      "Des guides pas à pas pour chaque type de graphique dans UniGraph, pensés pour créer des figures académiques claires sans commencer par le code.",
    authorLabel: "Standard auteur",
    quickEyebrow: "Démarrage rapide",
    quick1: "Importez un fichier Excel ou CSV.",
    quick2: "Choisissez la spécialité et le type de graphique.",
    quick3: "Sélectionnez les plages X/Y verticalement ou horizontalement.",
    quick4: "Réglez les paramètres d'image, puis créez le graphique.",
    tocAria: "Catégories de tutoriels",
    tocScatter: "Nuage",
    tocLine: "Courbe",
    tocBar: "Barres",
    tocHist: "Histogramme",
    tocPie: "Camembert",
    tocWaterfall: "Cascade",
    tocRisk: "Risque-rendement",
    tocPortfolio: "Portefeuille",
    tocCumulative: "Cumulé",
    tocCorr: "Carte thermique",
    tocDual: "Double axe Y",
    tocAnalysis: "Analyse",
    footerAuthor: "Standard auteur des tutoriels : Bowen",
    scatterTitle: "Nuage de points",
    scatterUse: "Idéal pour les mesures de laboratoire où chaque point est une paire X/Y observée.",
    scatterStep1: "Choisissez Graphique X/Y manuel, puis Nuage de points.",
    scatterStep2: "Définissez les plages X et Y ; le mode vertical signifie une colonne et des lignes début/fin.",
    scatterStep3: "Ouvrez les paramètres d'image pour nommer les axes, unités, couleurs et titre.",
    scatterStep4: "Activez l'ajustement ou l'analyse en un clic pour obtenir la régression.",
    scatterTip: "Astuce : pour un rapport de physique, gardez le style académique et ajoutez les barres d'erreur si disponibles.",
    lineTitle: "Courbe",
    lineUse: "Idéal pour les tendances dans le temps, le courant, la tension ou une variable ordonnée.",
    lineStep1: "Sélectionnez Courbe après l'import des données.",
    lineStep2: "Vérifiez que les valeurs X sont ordonnées.",
    lineStep3: "Utilisez le style académique pour des lignes fines et des points plus nets.",
    lineStep4: "Activez la notation scientifique si les graduations sont trop longues.",
    lineTip: "Astuce : utilisez une courbe pour une tendance continue, pas pour des catégories indépendantes.",
    barTitle: "Graphique en barres",
    barUse: "Idéal pour comparer des catégories comme dépenses, départements ou groupes d'expérience.",
    barStep1: "Utilisez les visualisations comptables ou le mode X/Y manuel, puis Barres.",
    barStep2: "Choisissez une colonne de catégories et une colonne numérique.",
    barStep3: "Gardez des étiquettes courtes ; faites-les pivoter si elles sont longues.",
    barStep4: "Ajoutez un titre et des unités pour clarifier le sens.",
    barTip: "Astuce : triez les valeurs avant l'import pour obtenir un classement.",
    histTitle: "Histogramme",
    histUse: "Idéal pour voir la distribution d'une variable numérique.",
    histStep1: "Sélectionnez Histogramme et choisissez une plage numérique.",
    histStep2: "Utilisez une seule variable ; les catégories ne conviennent pas ici.",
    histStep3: "Observez le centre, l'asymétrie et les valeurs atypiques.",
    histStep4: "Ajoutez un titre clair décrivant l'échantillon.",
    histTip: "Astuce : l'histogramme montre la dispersion ; les barres comparent des catégories.",
    pieTitle: "Camembert",
    pieUse: "Idéal pour montrer une composition, par exemple des parts de dépenses ou de portefeuille.",
    pieStep1: "Choisissez les visualisations comptables, puis Camembert.",
    pieStep2: "Définissez la colonne de catégories et la colonne de valeurs.",
    pieStep3: "Utilisez des valeurs positives et évitez trop de parts.",
    pieStep4: "Regroupez les petites catégories avant l'import si nécessaire.",
    pieTip: "Astuce : un camembert fonctionne mieux avec 3 à 6 catégories.",
    waterfallTitle: "Cascade de trésorerie",
    waterfallUse: "Idéal pour expliquer comment les entrées et sorties construisent un résultat final.",
    waterfallStep1: "Choisissez les visualisations comptables, puis Cascade de trésorerie.",
    waterfallStep2: "Utilisez une colonne d'étiquettes et une colonne de montants signés.",
    waterfallStep3: "Les valeurs positives augmentent le total ; les négatives le réduisent.",
    waterfallStep4: "Utilisez un titre comme Mouvement mensuel de trésorerie.",
    waterfallTip: "Astuce : la cascade explique mieux le mouvement financier qu'un graphique en barres ordinaire.",
    riskTitle: "Risque-rendement",
    riskUse: "Idéal pour comparer des actifs par volatilité et rendement moyen.",
    riskStep1: "Choisissez Finance, puis Risque-rendement.",
    riskStep2: "Sélectionnez au moins deux colonnes de prix ou valeurs d'actifs.",
    riskStep3: "UniGraph calcule les rendements, l'écart type et le rendement moyen.",
    riskStep4: "Vers la droite indique plus de risque ; vers le haut plus de rendement.",
    riskTip: "Astuce : utilisez le même intervalle de dates pour tous les actifs.",
    portfolioTitle: "Graphique de portefeuille",
    portfolioUse: "Idéal pour montrer l'allocation des actifs sélectionnés.",
    portfolioStep1: "Choisissez Finance, puis Portefeuille.",
    portfolioStep2: "Sélectionnez les colonnes d'actifs à inclure.",
    portfolioStep3: "Utilisez des noms d'actifs clairs dans les en-têtes.",
    portfolioStep4: "Utilisez ce graphique comme résumé visuel, pas comme conseil financier.",
    portfolioTip: "Astuce : gardez des noms courts pour des étiquettes lisibles.",
    cumulativeTitle: "Rendement cumulé",
    cumulativeUse: "Idéal pour comparer les trajectoires de croissance des actifs.",
    cumulativeStep1: "Choisissez Finance, puis Rendements cumulés.",
    cumulativeStep2: "Sélectionnez des colonnes d'actifs alignées par dates ou périodes.",
    cumulativeStep3: "Utilisez la légende pour comparer les trajectoires.",
    cumulativeStep4: "Vérifiez les sauts soudains pour détecter les données manquantes ou anormales.",
    cumulativeTip: "Astuce : nettoyez les valeurs manquantes avant de comparer plusieurs actifs.",
    corrTitle: "Carte de corrélation",
    corrUse: "Idéal pour voir si des actifs évoluent ensemble ou indépendamment.",
    corrStep1: "Choisissez Finance, puis Carte de corrélation.",
    corrStep2: "Sélectionnez plusieurs colonnes d'actifs.",
    corrStep3: "Une valeur proche de 1 indique une forte corrélation positive.",
    corrStep4: "Une valeur proche de 0 indique une relation plus faible.",
    corrTip: "Astuce : la corrélation est utile, mais ne prouve pas la causalité.",
    dualTitle: "Graphique à double axe Y",
    dualUse: "Idéal pour combiner deux graphiques enregistrés avec des unités Y différentes.",
    dualStep1: "Créez le premier graphique et gardez-le dans le gestionnaire de figures.",
    dualStep2: "Cliquez sur Nouvelle figure et créez le second graphique.",
    dualStep3: "Cliquez sur Double axe Y et choisissez les figures à combiner.",
    dualStep4: "Nommez le graphique combiné et vérifiez les deux axes.",
    dualTip: "Astuce : utilisez deux axes seulement si les variables partagent le même sens de X.",
    analysisTitle: "Analyse en un clic",
    analysisUse: "Idéal pour les rapports demandant pente, intercept, équation, r et R².",
    analysisStep1: "Créez d'abord un graphique X/Y manuel.",
    analysisStep2: "Cliquez sur Analyse en un clic dans le panneau gauche.",
    analysisStep3: "Choisissez la plage X utilisée pour la régression.",
    analysisStep4: "Sélectionnez les résultats à ajouter au graphique.",
    analysisTip: "Astuce : indiquez l'équation et R² pour expliquer une relation linéaire.",
  },
};

const tutorialLanguageSelect = document.querySelector("#tutorialLanguageSelect");
const tutorialMetaDescription = document.querySelector('meta[name="description"]');
const tutorialHeader = document.querySelector(".site-header");
const tutorialMotionQuery = window.matchMedia("(prefers-reduced-motion: reduce)");

function normalizeTutorialLanguage(language) {
  if (language && language.startsWith("zh")) {
    return "zh";
  }
  if (language && language.startsWith("fr")) {
    return "fr";
  }
  return "en";
}

function getInitialTutorialLanguage() {
  const saved = localStorage.getItem("unigraph-site-language");
  if (tutorialTranslations[saved]) {
    return saved;
  }
  return normalizeTutorialLanguage(navigator.language || "en");
}

function tutorialDictionary(language) {
  const selected = tutorialTranslations[language] ? language : "en";
  return { selected, dictionary: { ...tutorialTranslations.en, ...tutorialTranslations[selected] } };
}

function setTutorialLanguage(language) {
  const { selected, dictionary } = tutorialDictionary(language);
  document.documentElement.lang = selected === "zh" ? "zh-CN" : selected;
  document.title = dictionary.pageTitle;
  if (tutorialMetaDescription) {
    tutorialMetaDescription.setAttribute("content", dictionary.metaDescription);
  }
  document.querySelectorAll("[data-tutorial-i18n]").forEach((element) => {
    const key = element.getAttribute("data-tutorial-i18n");
    if (dictionary[key]) {
      element.textContent = dictionary[key];
    }
  });
  document.querySelectorAll("[data-tutorial-aria]").forEach((element) => {
    const key = element.getAttribute("data-tutorial-aria");
    if (dictionary[key]) {
      element.setAttribute("aria-label", dictionary[key]);
    }
  });
  tutorialLanguageSelect.value = selected;
  localStorage.setItem("unigraph-site-language", selected);
}

tutorialLanguageSelect.addEventListener("change", (event) => {
  setTutorialLanguage(event.target.value);
});

function setupTutorialMotion() {
  if (tutorialMotionQuery.matches) {
    document.documentElement.classList.add("reduce-motion");
    return;
  }
  const elements = [".tutorial-hero", ".tutorial-toc", ".tutorial-card"];
  document.querySelectorAll(elements.join(",")).forEach((element, index) => {
    element.classList.add("reveal");
    element.style.setProperty("--reveal-delay", `${Math.min(index * 45, 420)}ms`);
  });
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: "0px 0px -6% 0px" },
  );
  document.querySelectorAll(".reveal").forEach((element) => observer.observe(element));
  window.addEventListener(
    "scroll",
    () => {
      tutorialHeader.classList.toggle("is-scrolled", (window.scrollY || 0) > 24);
    },
    { passive: true },
  );
}

setTutorialLanguage(getInitialTutorialLanguage());
setupTutorialMotion();
