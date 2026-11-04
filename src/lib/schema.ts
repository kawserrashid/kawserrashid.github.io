// Shared Zod building blocks used by content.config.ts and profile.ts.
import { z } from 'astro/zod';

// "[Something]" marks a fact Kawser hasn't supplied yet (NFR-07).
// Fields that hold numbers, enums, URLs or emails accept a placeholder
// instead, so sample content can build without inventing facts.
export const placeholder = z
  .string()
  .regex(/^\[.+\]$/, 'Placeholders must be wrapped in [brackets]');

export const orPlaceholder = <T extends z.ZodType>(schema: T) =>
  z.union([schema, placeholder]);

export const statusEnum = z.enum(['planning', 'ongoing', 'completed']);
