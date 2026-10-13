// Helpers de renderização usados pelas páginas.

export const PLACEHOLDER_IMG = 'img/placeholder.svg';

export function escapeHtml(value) {
  return String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');
}

// Só aceita http(s): evita `javascript:` vindo do banco em atributos href/src.
export function safeUrl(value, fallback = '') {
  try {
    const url = new URL(value);
    return url.protocol === 'http:' || url.protocol === 'https:' ? url.href : fallback;
  } catch {
    return fallback;
  }
}

export function gradeBadgeColor(grade) {
  if (grade >= 9) return 'bg-success';
  if (grade >= 8) return 'bg-warning text-dark';
  return 'bg-secondary';
}

export function formatDateBR(isoDate) {
  const parts = String(isoDate ?? '').split('-');
  return parts.length === 3 ? `${parts[2]}/${parts[1]}/${parts[0]}` : String(isoDate ?? '');
}

export function formatBRL(value) {
  return Number(value).toFixed(2).replace('.', ',');
}

export function todayLocal() {
  const d = new Date();
  const pad = (n) => String(n).padStart(2, '0');
  return `${d.getFullYear()}-${pad(d.getMonth() + 1)}-${pad(d.getDate())}`;
}

export function errorMessage(error) {
  if (!error) return 'Erro desconhecido';
  if (error.code === '23503') return 'Graduadora em uso por cartas ou inexistente.';
  if (error.code === '23505') return 'Registro duplicado.';
  if (error.code === '42501') return 'Sem permissão. Entre com a conta de administrador.';
  return error.message || String(error);
}
