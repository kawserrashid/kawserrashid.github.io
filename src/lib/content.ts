// Query helpers: the site's "repository layer". Pages call these instead of
// filtering/sorting collections themselves.
import { getCollection, type CollectionEntry } from 'astro:content';

const newestFirst = (a: Date, b: Date) => b.getTime() - a.getTime();

/** Published research write-ups, newest first. */
export async function getResearch(limit?: number) {
  const items = await getCollection('research', ({ data }) => !data.draft);
  return items.sort((a, b) => newestFirst(a.data.date, b.data.date)).slice(0, limit);
}

/** URL of a write-up's own page (FR-14). The file name is the slug. */
export const researchUrl = (entry: CollectionEntry<'research'>) => `/research/${entry.id}/`;

/** Published notes, newest first. */
export async function getNotes(limit?: number) {
  const items = await getCollection('notes', ({ data }) => !data.draft);
  return items.sort((a, b) => newestFirst(a.data.date, b.data.date)).slice(0, limit);
}

/** Paper notes, most recently written first. */
export async function getPaperNotes(limit?: number) {
  const items = await getCollection('paperNotes');
  return items.sort((a, b) => newestFirst(a.data.written, b.data.written)).slice(0, limit);
}

export type Publication = CollectionEntry<'publications'>['data'];
export type NumberedPublication = Publication & { number: number };

/**
 * Publications split into the two display groups, with numbering that
 * continues across groups (1 = conference paper, 2… = manuscripts & thesis).
 * Within a group, file order is kept.
 */
export async function getPublicationGroups() {
  const all = (await getCollection('publications')).map((e) => e.data);
  const conference = all.filter((p) => p.type === 'conference');
  const other = all.filter((p) => p.type !== 'conference');
  let n = 0;
  const number = (list: Publication[]): NumberedPublication[] =>
    list.map((p) => ({ ...p, number: ++n }));
  return [
    { label: 'Conference paper', items: number(conference) },
    { label: 'Manuscripts & thesis', items: number(other) },
  ].filter((g) => g.items.length > 0);
}
