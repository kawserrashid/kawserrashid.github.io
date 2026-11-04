// Status → label, icon, color. One place, used by StatusBadge and StatusLegend.
import type { z } from 'astro/zod';
import type { statusEnum } from './schema';
import Lightbulb from '@lucide/astro/icons/lightbulb';
import LoaderCircle from '@lucide/astro/icons/loader-circle';
import CheckCheck from '@lucide/astro/icons/check-check';

export type Status = z.infer<typeof statusEnum>;

export const statuses = {
  planning: { label: 'Planning', blurb: 'early idea', icon: Lightbulb, color: 'var(--color-olive-light)' },
  ongoing: { label: 'Ongoing', blurb: 'in progress', icon: LoaderCircle, color: 'var(--color-sand)' },
  completed: { label: 'Completed', blurb: 'finished work', icon: CheckCheck, color: 'var(--color-teal)' },
} as const;
