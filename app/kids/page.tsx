'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { useAuth } from '@/components/auth-provider';
import { loadKids, saveKid, deleteKid } from '@/lib/firestore';
import { Nav } from '@/components/nav';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Label } from '@/components/ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Alert, AlertDescription } from '@/components/ui/alert';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { Separator } from '@/components/ui/separator';
import { AVAILABLE_GRADES, type KidProfile } from '@/types';
import { Pencil, Trash2, AlertCircle } from 'lucide-react';

const CA_PROVINCES = [
  ['AB', 'Alberta'], ['BC', 'British Columbia'], ['MB', 'Manitoba'],
  ['NB', 'New Brunswick'], ['NL', 'Newfoundland and Labrador'],
  ['NT', 'Northwest Territories'], ['NS', 'Nova Scotia'], ['NU', 'Nunavut'],
  ['ON', 'Ontario'], ['PE', 'Prince Edward Island'], ['QC', 'Quebec'],
  ['SK', 'Saskatchewan'], ['YT', 'Yukon'],
];

const US_STATES = [
  ['AL','Alabama'],['AK','Alaska'],['AZ','Arizona'],['AR','Arkansas'],
  ['CA','California'],['CO','Colorado'],['CT','Connecticut'],['DE','Delaware'],
  ['FL','Florida'],['GA','Georgia'],['HI','Hawaii'],['ID','Idaho'],
  ['IL','Illinois'],['IN','Indiana'],['IA','Iowa'],['KS','Kansas'],
  ['KY','Kentucky'],['LA','Louisiana'],['ME','Maine'],['MD','Maryland'],
  ['MA','Massachusetts'],['MI','Michigan'],['MN','Minnesota'],['MS','Mississippi'],
  ['MO','Missouri'],['MT','Montana'],['NE','Nebraska'],['NV','Nevada'],
  ['NH','New Hampshire'],['NJ','New Jersey'],['NM','New Mexico'],['NY','New York'],
  ['NC','North Carolina'],['ND','North Dakota'],['OH','Ohio'],['OK','Oklahoma'],
  ['OR','Oregon'],['PA','Pennsylvania'],['RI','Rhode Island'],['SC','South Carolina'],
  ['SD','South Dakota'],['TN','Tennessee'],['TX','Texas'],['UT','Utah'],
  ['VT','Vermont'],['VA','Virginia'],['WA','Washington'],['WV','West Virginia'],
  ['WI','Wisconsin'],['WY','Wyoming'],
];

function gradeLabel(g: number) {
  return g === 0 ? 'Kindergarten' : `Grade ${g}`;
}

const BLANK = { name: '', grade: '2', country: 'CA' as 'CA' | 'US', province: 'ON' };

export default function KidsPage() {
  const { user, loading } = useAuth();
  const router = useRouter();
  const [kids, setKids] = useState<KidProfile[]>([]);
  const [kidsLoading, setKidsLoading] = useState(true);

  // Form state
  const [editId, setEditId] = useState<string | null>(null);
  const [name, setName] = useState(BLANK.name);
  const [grade, setGrade] = useState(BLANK.grade);
  const [country, setCountry] = useState<'CA' | 'US'>(BLANK.country);
  const [province, setProvince] = useState(BLANK.province);
  const [busy, setBusy] = useState(false);
  const [formError, setFormError] = useState('');

  useEffect(() => {
    if (!loading && !user) router.replace('/auth');
  }, [user, loading, router]);

  useEffect(() => {
    if (!user) return;
    loadKids(user.uid)
      .then(setKids)
      .finally(() => setKidsLoading(false));
  }, [user]);

  const regions = country === 'CA' ? CA_PROVINCES : US_STATES;
  const regionSupported = country === 'CA' && province === 'ON';

  function resetForm() {
    setEditId(null);
    setName(BLANK.name);
    setGrade(BLANK.grade);
    setCountry(BLANK.country);
    setProvince(BLANK.province);
    setFormError('');
  }

  function startEdit(kid: KidProfile) {
    setEditId(kid.id);
    setName(kid.name);
    setGrade(String(kid.grade));
    setCountry(kid.country);
    setProvince(kid.province);
    setFormError('');
    window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
  }

  async function handleDelete(kid: KidProfile) {
    if (!user) return;
    if (!confirm(`Delete ${kid.name} and all their quiz progress? This cannot be undone.`)) return;
    await deleteKid(user.uid, kid.id);
    setKids((prev) => prev.filter((k) => k.id !== kid.id));
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    if (!user) return;
    if (!regionSupported) {
      setFormError('Curriculum for this province/state is coming soon — currently only Ontario, Canada is supported.');
      return;
    }
    setFormError('');
    setBusy(true);
    try {
      const id = await saveKid(
        user.uid,
        { name: name.trim(), grade: parseInt(grade, 10), country, province },
        editId,
      );
      const updated = await loadKids(user.uid);
      setKids(updated);
      resetForm();
      if (!editId) {
        // Scroll to newly added kid
        const el = document.getElementById(`kid-${id}`);
        el?.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    } catch {
      setFormError('Failed to save. Please try again.');
    } finally {
      setBusy(false);
    }
  }

  if (loading || !user) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <p className="text-muted-foreground text-sm">Loading…</p>
      </div>
    );
  }

  return (
    <div className="flex flex-col min-h-screen">
      <Nav />

      <main className="flex-1 mx-auto w-full max-w-2xl px-4 py-8">
        <h1 className="text-2xl font-bold mb-1">Manage Children</h1>
        <p className="text-sm text-muted-foreground mb-6">
          Add each child with their name, grade, and location. Progress is tracked separately per child.
        </p>

        {/* Kids list */}
        {kidsLoading ? (
          <p className="text-sm text-muted-foreground">Loading…</p>
        ) : kids.length === 0 ? (
          <p className="text-sm text-muted-foreground mb-6">
            No children added yet. Use the form below to add your first child.
          </p>
        ) : (
          <div className="space-y-3 mb-8">
            {kids.map((kid) => {
              const hasContent =
                AVAILABLE_GRADES.includes(kid.grade) && kid.country === 'CA' && kid.province === 'ON';
              return (
                <div
                  id={`kid-${kid.id}`}
                  key={kid.id}
                  className="flex items-center justify-between rounded-lg border border-border px-4 py-3 bg-card"
                >
                  <div>
                    <p className="font-medium">{kid.name}</p>
                    <p className="text-sm text-muted-foreground">
                      {gradeLabel(kid.grade)} · {kid.province}, {kid.country}
                      {!hasContent && (
                        <span className="ml-2 text-amber-600">(curriculum coming soon)</span>
                      )}
                    </p>
                  </div>
                  <div className="flex gap-2">
                    <Button variant="ghost" size="icon" onClick={() => startEdit(kid)} aria-label="Edit">
                      <Pencil className="h-4 w-4" />
                    </Button>
                    <Button
                      variant="ghost"
                      size="icon"
                      onClick={() => handleDelete(kid)}
                      aria-label="Delete"
                      className="text-destructive hover:text-destructive"
                    >
                      <Trash2 className="h-4 w-4" />
                    </Button>
                  </div>
                </div>
              );
            })}
          </div>
        )}

        <Separator className="mb-8" />

        {/* Add / Edit form */}
        <Card>
          <CardHeader>
            <CardTitle>{editId ? 'Edit Child' : 'Add a Child'}</CardTitle>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-1.5">
                <Label htmlFor="kid-name">Child&apos;s name</Label>
                <Input
                  id="kid-name"
                  placeholder="e.g. Ahmed"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  required
                  autoComplete="off"
                />
              </div>

              <div className="space-y-1.5">
                <Label htmlFor="kid-grade">Grade entering in September</Label>
                <Select value={grade} onValueChange={setGrade}>
                  <SelectTrigger id="kid-grade">
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    {Array.from({ length: 13 }, (_, i) => i).map((g) => (
                      <SelectItem key={g} value={String(g)}>
                        {gradeLabel(g)}
                      </SelectItem>
                    ))}
                  </SelectContent>
                </Select>
              </div>

              <div className="grid grid-cols-2 gap-4">
                <div className="space-y-1.5">
                  <Label htmlFor="kid-country">Country</Label>
                  <Select
                    value={country}
                    onValueChange={(v) => {
                      setCountry(v as 'CA' | 'US');
                      setProvince(v === 'CA' ? 'ON' : 'AL');
                    }}
                  >
                    <SelectTrigger id="kid-country">
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectItem value="CA">Canada</SelectItem>
                      <SelectItem value="US">United States</SelectItem>
                    </SelectContent>
                  </Select>
                </div>

                <div className="space-y-1.5">
                  <Label htmlFor="kid-province">{country === 'CA' ? 'Province / Territory' : 'State'}</Label>
                  <Select value={province} onValueChange={setProvince}>
                    <SelectTrigger id="kid-province">
                      <SelectValue />
                    </SelectTrigger>
                    <SelectContent>
                      {regions.map(([code, label]) => (
                        <SelectItem key={code} value={code}>{label}</SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>
              </div>

              {!regionSupported && (
                <Alert>
                  <AlertCircle className="h-4 w-4" />
                  <AlertDescription>
                    {country === 'CA'
                      ? `Curriculum for ${regions.find(([code]) => code === province)?.[1] ?? 'this province'} is coming soon — currently only Ontario is available.`
                      : `Curriculum for ${regions.find(([code]) => code === province)?.[1] ?? 'this state'} is coming soon — GradesBooster currently only supports Ontario, Canada.`}
                  </AlertDescription>
                </Alert>
              )}

              {formError && (
                <Alert variant="destructive">
                  <AlertCircle className="h-4 w-4" />
                  <AlertDescription>{formError}</AlertDescription>
                </Alert>
              )}

              <div className="flex gap-3 pt-1">
                <Button type="submit" disabled={busy || !regionSupported}>
                  {busy ? (editId ? 'Updating…' : 'Saving…') : (editId ? 'Update Child' : 'Save Child')}
                </Button>
                {editId && (
                  <Button type="button" variant="outline" onClick={resetForm}>
                    Cancel
                  </Button>
                )}
              </div>
            </form>
          </CardContent>
        </Card>
      </main>
    </div>
  );
}
