// Loads home.json (all Home page copy) and validates it at build time.
// A missing or empty field fails the build with the field's path.
import { z } from 'astro/zod';
import raw from '../data/home.json';

const text = z.string().min(1);
const titled = z.object({ title: text, hint: text });

const homeSchema = z.object({
  hero: z.object({ sub: text, primaryButton: text, secondaryButton: text }),
  sketchBoard: z.object({ title: text, intro: text }),
  research: titled,
  notes: titled,
  paperNotes: titled,
  publications: z.object({ title: text, cvLink: text }),
  now: z.object({ title: text }),
  cta: z.object({ title: text, text: text, button: text }),
});

export const home = homeSchema.parse(raw);
