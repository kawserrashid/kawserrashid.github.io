// Small display helpers.

/** "2026-11" → "November 2026" */
export function formatMonth(yyyyMm: string) {
  const [y, m] = yyyyMm.split('-').map(Number);
  return new Date(Date.UTC(y, m - 1, 1)).toLocaleDateString('en-US', {
    month: 'long',
    year: 'numeric',
    timeZone: 'UTC',
  });
}

/** Date → "4 November 2026" (UTC, so build machine timezone can't shift it). */
export function formatDate(d: Date) {
  return d.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric', timeZone: 'UTC' });
}

const pubStatusLabels: Record<string, string> = {
  'under-review': 'Under review',
  'in-preparation': 'In preparation',
};

/** Enum value → label; placeholders like "[In preparation]" pass through unchanged. */
export const pubStatusLabel = (s: string) => pubStatusLabels[s] ?? s;

/**
 * Splits "I'm Kawser, an engineer…" around the first occurrence of `word`,
 * so the page can highlight it. Returns null if the word isn't there.
 */
export function splitOnWord(text: string, word: string) {
  const i = text.indexOf(word);
  return i === -1 ? null : { before: text.slice(0, i), word, after: text.slice(i + word.length) };
}

/** "plain **bold** plain" → [{ text, bold }] segments for minimal inline emphasis. */
export function boldSegments(text: string) {
  return text.split(/\*\*(.+?)\*\*/g).map((t, i) => ({ text: t, bold: i % 2 === 1 }));
}
