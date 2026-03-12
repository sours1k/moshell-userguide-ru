const data = await fetch("./guide-data.json").then((response) => response.json());

const pageNav = document.querySelector("#page-nav");
const sectionNav = document.querySelector("#section-nav");
const article = document.querySelector("#article");
const pageTitle = document.querySelector("#page-title");
const pageSubtitle = document.querySelector("#page-subtitle");
const searchInput = document.querySelector("#search");
const pager = document.querySelector("#pager");
const pageNumber = document.querySelector("#page-number");
const sectionCount = document.querySelector("#section-count");

const ui = data.ui ?? {};

const uiBindings = [
  ["#brand-title", "brand_title"],
  ["#brand-description", "brand_description"],
  ["#nav-title", "nav_title"],
  ["#nav-caption", "nav_caption"],
  ["#search-label", "search_label"],
  ["#hero-eyebrow", "hero_eyebrow"],
  ["#hero-card-title", "hero_card_title"],
  ["#hero-card-description", "hero_card_description"],
  ["#toc-title", "toc_title"],
  ["#page-meta-label", "page_meta"],
  ["#section-meta-label", "section_meta"],
];

for (const [selector, key] of uiBindings) {
  const node = document.querySelector(selector);
  if (node && ui[key]) {
    node.textContent = ui[key];
  }
}

if (ui.search_placeholder) {
  searchInput.placeholder = ui.search_placeholder;
}
if (ui.site_title) {
  document.title = ui.site_title;
}

const bySlug = new Map(data.pages.map((page) => [page.slug, page]));
let sectionObserver;

function currentSlug() {
  const hash = window.location.hash.replace(/^#/, "");
  const [pageSlug] = hash.split("::");
  return bySlug.has(pageSlug) ? pageSlug : data.pages[0]?.slug;
}

function pageLink(page) {
  const sectionCountLabel = page.sections.length ? `${page.sections.length}` : "0";
  return `
    <a class="page-link" href="#${page.slug}" data-slug="${page.slug}">
      <span class="page-link-title">${page.title}</span>
      <small>${page.titleEn}</small>
      <span class="page-chip">${sectionCountLabel}</span>
    </a>
  `;
}

function sectionLink(section) {
  const levelClass = section.level === 3 ? "is-child" : "";
  return `<a class="section-link ${levelClass}" href="#${currentSlug()}::${section.id}">${section.title}</a>`;
}

function setActiveLink(slug) {
  for (const link of document.querySelectorAll(".page-link")) {
    link.classList.toggle("active", link.dataset.slug === slug);
  }
}

function renderPageList(query = "") {
  const normalized = query.trim().toLowerCase();
  const filtered = normalized
    ? data.pages.filter((page) =>
        [page.title, page.titleEn, page.searchText].join(" ").toLowerCase().includes(normalized),
      )
    : data.pages;
  pageNav.innerHTML = filtered.length
    ? filtered.map(pageLink).join("")
    : `
      <div class="empty-state">
        <strong>${ui.empty_search ?? "Nothing found"}</strong>
        <p>${ui.empty_search_hint ?? "Try another term."}</p>
      </div>
    `;
  setActiveLink(currentSlug());
}

function renderPager(page) {
  const index = data.pages.findIndex((item) => item.slug === page.slug);
  const prev = data.pages[index - 1];
  const next = data.pages[index + 1];
  const prevLabel = ui.prev_page ?? "Previous";
  const nextLabel = ui.next_page ?? "Next";

  pager.innerHTML = `
    ${
      prev
        ? `<a class="pager-link" href="#${prev.slug}">
            <span>${prevLabel}</span>
            <strong>${prev.title}</strong>
          </a>`
        : `<span></span>`
    }
    ${
      next
        ? `<a class="pager-link is-next" href="#${next.slug}">
            <span>${nextLabel}</span>
            <strong>${next.title}</strong>
          </a>`
        : `<span></span>`
    }
  `;
}

function bindScrollSpy() {
  if (sectionObserver) {
    sectionObserver.disconnect();
  }

  const sections = [...document.querySelectorAll(".article h2[id], .article h3[id]")];
  if (!sections.length) {
    return;
  }

  const sectionLinks = [...document.querySelectorAll(".section-link")];
  sectionObserver = new IntersectionObserver(
    (entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
      if (!visible) {
        return;
      }
      for (const link of sectionLinks) {
        link.classList.toggle("active", link.getAttribute("href") === `#${currentSlug()}::${visible.target.id}`);
      }
    },
    { rootMargin: "-20% 0px -60% 0px", threshold: [0, 1] },
  );

  for (const section of sections) {
    sectionObserver.observe(section);
  }
}

function renderPage(slug) {
  const [pageSlug, anchor] = slug.split("::");
  const page = bySlug.get(pageSlug) ?? data.pages[0];
  if (!page) {
    return;
  }

  pageTitle.textContent = page.title;
  pageSubtitle.textContent = page.titleEn;
  article.innerHTML = page.content;
  sectionNav.innerHTML = page.sections.map(sectionLink).join("");
  pageNumber.textContent = String(data.pages.findIndex((item) => item.slug === page.slug) + 1);
  sectionCount.textContent = String(page.sections.length);
  setActiveLink(page.slug);
  renderPager(page);
  bindScrollSpy();

  if (anchor) {
    const target = document.getElementById(anchor);
    if (target) {
      requestAnimationFrame(() => target.scrollIntoView({ behavior: "smooth", block: "start" }));
    }
  } else {
    window.scrollTo({ top: 0, behavior: "auto" });
  }
}

window.addEventListener("hashchange", () => renderPage(window.location.hash.replace(/^#/, "")));

searchInput.addEventListener("input", (event) => {
  renderPageList(event.target.value);
});

renderPageList();
renderPage(window.location.hash.replace(/^#/, "") || currentSlug());
