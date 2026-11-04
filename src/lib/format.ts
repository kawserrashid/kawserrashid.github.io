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
