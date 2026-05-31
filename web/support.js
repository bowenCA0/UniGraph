const supportTranslations = {
  en: {
    pageTitle: "Support UniGraph",
    metaDescription:
      "Support UniGraph, a currently free student plotting project, through OKX crypto, Touch 'n Go, or Alipay.",
    brandAria: "Back to UniGraph home",
    navAria: "Support navigation",
    backHome: "Home",
    languageLabel: "Language",
    eyebrow: "Support UniGraph",
    title: "Keep a free learning tool moving forward",
    intro:
      "UniGraph is currently a fully free project for students and teachers. If it saves your time, helps your class, or makes data analysis less intimidating, your support becomes the fuel for updates, tutorials, and long-term maintenance.",
    statsAria: "Project values",
    statFree: "Free",
    statFreeText: "Current desktop features",
    statStudents: "Students",
    statStudentsText: "Physics, accounting, finance",
    statUpdates: "Updates",
    statUpdatesText: "Powered by support",
    workspaceAria: "Choose support method",
    chooseEyebrow: "Choose method",
    okxLabel: "Crypto",
    okxMenu: "For digital asset supporters",
    tngMenu: "For Malaysia-based supporters",
    aliLabel: "Alipay",
    aliMenu: "For Chinese users",
    securityNote:
      "Please confirm the payment details in your app before sending. Thank you for supporting a project that stays accessible to learners.",
    methods: {
      okx: {
        kicker: "Crypto",
        title: "OKX",
        description: "Scan the QR code with OKX or a compatible crypto wallet.",
        alt: "OKX crypto support QR code",
      },
      tng: {
        kicker: "Touch 'n Go",
        title: "TNG eWallet",
        description: "Scan the QR code with Touch 'n Go eWallet.",
        alt: "Touch 'n Go support QR code",
      },
      ali: {
        kicker: "Alipay",
        title: "Alipay",
        description: "Scan the QR code with Alipay.",
        alt: "Alipay support QR code",
      },
    },
  },
  zh: {
    pageTitle: "支持 UniGraph",
    metaDescription: "通过 OKX 加密货币、Touch 'n Go 或支付宝支持 UniGraph，一个目前完全免费的学生绘图项目。",
    brandAria: "返回 UniGraph 首页",
    navAria: "支持页面导航",
    backHome: "首页",
    languageLabel: "语言",
    eyebrow: "支持 UniGraph",
    title: "让免费的学习工具继续向前",
    intro:
      "UniGraph 目前是面向学生和老师完全免费的项目。如果它帮你节省了时间、帮助了课堂，或让数据分析变得不再吓人，你的支持就会成为更新、教程和长期维护的动力。",
    statsAria: "项目价值",
    statFree: "免费",
    statFreeText: "当前桌面端功能",
    statStudents: "学生",
    statStudentsText: "物理、会计、金融",
    statUpdates: "更新",
    statUpdatesText: "由支持驱动",
    workspaceAria: "选择支持方式",
    chooseEyebrow: "选择方式",
    okxLabel: "加密货币",
    okxMenu: "适合数字资产支持者",
    tngMenu: "适合马来西亚用户",
    aliLabel: "支付宝",
    aliMenu: "适合中国用户",
    securityNote: "付款前请在应用中确认收款信息。感谢你支持一个持续对学习者开放的项目。",
    methods: {
      okx: {
        kicker: "加密货币",
        title: "OKX",
        description: "请使用 OKX 或兼容的钱包扫描二维码。",
        alt: "OKX 加密货币打赏二维码",
      },
      tng: {
        kicker: "Touch 'n Go",
        title: "TNG 电子钱包",
        description: "请使用 Touch 'n Go eWallet 扫描二维码。",
        alt: "Touch 'n Go 打赏二维码",
      },
      ali: {
        kicker: "支付宝",
        title: "Alipay",
        description: "请使用支付宝扫描二维码。",
        alt: "支付宝打赏二维码",
      },
    },
  },
  fr: {
    pageTitle: "Soutenir UniGraph",
    metaDescription:
      "Soutenez UniGraph, un projet de tracé étudiant actuellement gratuit, avec OKX crypto, Touch 'n Go ou Alipay.",
    brandAria: "Retour à l'accueil UniGraph",
    navAria: "Navigation de soutien",
    backHome: "Accueil",
    languageLabel: "Langue",
    eyebrow: "Soutenir UniGraph",
    title: "Faire avancer un outil d'apprentissage gratuit",
    intro:
      "UniGraph est actuellement entièrement gratuit pour les étudiants et les enseignants. S'il vous fait gagner du temps, aide votre cours ou rend l'analyse de données moins intimidante, votre soutien alimente les mises à jour, les tutoriels et la maintenance.",
    statsAria: "Valeurs du projet",
    statFree: "Gratuit",
    statFreeText: "Fonctions bureau actuelles",
    statStudents: "Étudiants",
    statStudentsText: "Physique, comptabilité, finance",
    statUpdates: "Mises à jour",
    statUpdatesText: "Propulsées par le soutien",
    workspaceAria: "Choisir une méthode de soutien",
    chooseEyebrow: "Choisir une méthode",
    okxLabel: "Crypto",
    okxMenu: "Pour les soutiens en actifs numériques",
    tngMenu: "Pour les soutiens en Malaisie",
    aliLabel: "Alipay",
    aliMenu: "Pour les utilisateurs chinois",
    securityNote:
      "Veuillez vérifier les détails de paiement dans votre application avant l'envoi. Merci de soutenir un projet qui reste accessible aux apprenants.",
    methods: {
      okx: {
        kicker: "Crypto",
        title: "OKX",
        description: "Scannez le QR code avec OKX ou un portefeuille compatible.",
        alt: "QR code de soutien crypto OKX",
      },
      tng: {
        kicker: "Touch 'n Go",
        title: "TNG eWallet",
        description: "Scannez le QR code avec Touch 'n Go eWallet.",
        alt: "QR code de soutien Touch 'n Go",
      },
      ali: {
        kicker: "Alipay",
        title: "Alipay",
        description: "Scannez le QR code avec Alipay.",
        alt: "QR code de soutien Alipay",
      },
    },
  },
};

const methodImages = {
  okx: "./okx.png",
  tng: "./tng.png",
  ali: "./ali.png",
};

const languageSelect = document.querySelector("#supportLanguageSelect");
const metaDescription = document.querySelector('meta[name="description"]');
const methodKicker = document.querySelector("#methodKicker");
const methodTitle = document.querySelector("#methodTitle");
const methodDescription = document.querySelector("#methodDescription");
const methodQr = document.querySelector("#methodQr");
const methodButtons = Array.from(document.querySelectorAll(".payment-option"));
let currentLanguage = "en";
let currentMethod = "okx";

function normalizeLanguage(language) {
  if (language && language.startsWith("zh")) {
    return "zh";
  }
  if (language && language.startsWith("fr")) {
    return "fr";
  }
  return "en";
}

function getInitialLanguage() {
  const saved = localStorage.getItem("unigraph-site-language");
  if (supportTranslations[saved]) {
    return saved;
  }
  return normalizeLanguage(navigator.language || "en");
}

function setLanguage(language) {
  currentLanguage = supportTranslations[language] ? language : "en";
  const dictionary = supportTranslations[currentLanguage];
  document.documentElement.lang = currentLanguage === "zh" ? "zh-CN" : currentLanguage;
  document.title = dictionary.pageTitle;
  if (metaDescription) {
    metaDescription.setAttribute("content", dictionary.metaDescription);
  }

  document.querySelectorAll("[data-support-i18n]").forEach((element) => {
    const key = element.getAttribute("data-support-i18n");
    if (dictionary[key]) {
      element.textContent = dictionary[key];
    }
  });

  document.querySelectorAll("[data-support-aria]").forEach((element) => {
    const key = element.getAttribute("data-support-aria");
    if (dictionary[key]) {
      element.setAttribute("aria-label", dictionary[key]);
    }
  });

  languageSelect.value = currentLanguage;
  localStorage.setItem("unigraph-site-language", currentLanguage);
  setMethod(currentMethod);
}

function setMethod(method) {
  currentMethod = supportTranslations[currentLanguage].methods[method] ? method : "okx";
  const details = supportTranslations[currentLanguage].methods[currentMethod];
  methodKicker.textContent = details.kicker;
  methodTitle.textContent = details.title;
  methodDescription.textContent = details.description;
  methodQr.src = methodImages[currentMethod];
  methodQr.alt = details.alt;

  methodButtons.forEach((button) => {
    const isActive = button.dataset.method === currentMethod;
    button.classList.toggle("active", isActive);
    button.setAttribute("aria-pressed", String(isActive));
  });
}

languageSelect.addEventListener("change", (event) => {
  setLanguage(event.target.value);
});

methodButtons.forEach((button) => {
  button.addEventListener("click", () => setMethod(button.dataset.method));
});

setLanguage(getInitialLanguage());
