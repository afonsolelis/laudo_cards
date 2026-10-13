// Cliente Supabase compartilhado pelas páginas.
// A chave publishable é pública por design: quem protege os dados é o RLS
// definido em supabase/schema.sql.
import { createClient } from 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.58.0/+esm';

export const SUPABASE_URL = 'https://lwamaovuxcevsjfvtqhf.supabase.co';
export const SUPABASE_PUBLISHABLE_KEY = 'sb_publishable_j0O_u0t7-lDCtBbmqaIz3A_8vAIGcyJ';
export const IMAGE_BUCKET = 'card-images';

export const supabase = createClient(SUPABASE_URL, SUPABASE_PUBLISHABLE_KEY);

export async function getSession() {
  const { data } = await supabase.auth.getSession();
  return data.session;
}
