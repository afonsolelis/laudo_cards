// Dados e helpers compartilhados pelas páginas.
// O acervo vive em data/cards.json (site 100% estático, sem backend).

export const PLACEHOLDER_IMG = 'img/placeholder.svg';

// Graduadoras já publicadas no site. As demais aparecem como "Em breve".
export const ACTIVE_GRADERS = ['GRADD'];

let cardsPromise;

export function loadCards() {
  cardsPromise ??= fetch('data/cards.json', { cache: 'no-cache' }).then((res) => {
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return res.json();
  });
  return cardsPromise;
}

export function graderSlug(name) {
  return String(name ?? '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

export function escapeHtml(value) {
  return String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');
}

// Só aceita http(s): evita `javascript:` vindo dos dados em atributos href/src.
export function safeUrl(value, fallback = '') {
  try {
    const url = new URL(value);
    return url.protocol === 'http:' || url.protocol === 'https:' ? url.href : fallback;
  } catch {
    return fallback;
  }
}

// Nota exibida: cartas só autenticadas (final 0/nulo) mostram "A".
export function gradeLabel(grade) {
  const final = grade?.final;
  return final ? String(final) : 'A';
}

export function formatDateBR(isoDate) {
  const parts = String(isoDate ?? '').split('-');
  return parts.length === 3 ? `${parts[2]}/${parts[1]}/${parts[0]}` : String(isoDate ?? '');
}

export function formatBRL(value) {
  return Number(value).toLocaleString('pt-BR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
}
