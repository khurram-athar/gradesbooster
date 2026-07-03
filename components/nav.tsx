'use client';

import Link from 'next/link';
import { useRouter, usePathname } from 'next/navigation';
import { DropdownMenu } from 'radix-ui';
import { useAuth } from '@/components/auth-provider';
import { Button } from '@/components/ui/button';
import Image from 'next/image';
import {
  LayoutDashboard,
  Users,
  LogOut,
  Info,
  ChevronDown,
  HelpCircle,
  Shield,
  Home,
  MessageSquareHeart,
  Menu,
} from 'lucide-react';

export function Nav() {
  const { user, logOut } = useAuth();
  const router = useRouter();
  const pathname = usePathname();

  const handleSignOut = async () => {
    await logOut();
    router.push('/auth');
  };

  if (!user) return null;

  const navLinks = [
    { href: '/home', label: 'My Kids', icon: Users },
    { href: '/dashboard', label: 'Dashboard', icon: LayoutDashboard },
  ];

  const infoLinks = [
    { href: '/', label: 'Homepage', icon: Home },
    { href: '/#how-it-works', label: 'How It Works', icon: Info },
    { href: '/#faq', label: 'FAQ', icon: HelpCircle },
    { href: '/privacy', label: 'Privacy Policy', icon: Shield },
    { href: '/feedback', label: 'Send Feedback', icon: MessageSquareHeart },
  ];

  return (
    <header className="sticky top-0 z-50 border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="mx-auto max-w-6xl px-4 h-14 grid grid-cols-[1fr_auto_1fr] items-center">

        {/* Left: quick-access links (desktop only) */}
        <nav className="hidden sm:flex items-center gap-1 justify-self-start">
          {navLinks.map(({ href, label, icon: Icon }) => (
            <Link
              key={href}
              href={href}
              className={`flex items-center gap-1.5 px-3 py-1.5 rounded-md text-sm font-medium transition-colors ${
                pathname === href
                  ? 'bg-muted text-foreground'
                  : 'text-muted-foreground hover:text-foreground hover:bg-muted'
              }`}
            >
              <Icon className="h-4 w-4" />
              {label}
            </Link>
          ))}
        </nav>

        {/* Center: logo → app home */}
        <Link href="/home" className="flex items-center justify-self-center">
          <Image src="/logo.svg" alt="GradesBooster" width={160} height={38} priority />
        </Link>

        {/* Right: Menu dropdown + user + sign out */}
        <div className="flex items-center gap-2 justify-self-end">
          <DropdownMenu.Root>
            <DropdownMenu.Trigger asChild>
              <button
                aria-label="Open menu"
                className="flex items-center gap-1.5 px-3 py-1.5 rounded-md text-sm font-medium text-foreground border border-border hover:bg-muted transition-colors outline-none"
              >
                <Menu className="h-4 w-4" />
                <span className="hidden sm:inline">Menu</span>
                <ChevronDown className="h-3 w-3 opacity-60" />
              </button>
            </DropdownMenu.Trigger>

            <DropdownMenu.Portal>
              <DropdownMenu.Content
                align="end"
                sideOffset={6}
                className="z-50 min-w-[200px] rounded-xl border border-border bg-card shadow-lg py-1.5 outline-none animate-in fade-in-0 zoom-in-95"
              >
                <div className="sm:hidden px-3 py-2">
                  {navLinks.map(({ href, label, icon: Icon }) => (
                    <DropdownMenu.Item key={href} asChild>
                      <Link
                        href={href}
                        className="flex items-center gap-2.5 px-0 py-2 text-sm text-foreground hover:bg-muted rounded-md cursor-pointer outline-none transition-colors"
                      >
                        <Icon className="h-4 w-4 text-muted-foreground shrink-0" />
                        {label}
                      </Link>
                    </DropdownMenu.Item>
                  ))}
                  <div className="my-1 h-px bg-border" />
                </div>
                {infoLinks.map(({ href, label, icon: Icon }) => (
                  <DropdownMenu.Item key={href} asChild>
                    <Link
                      href={href}
                      className="flex items-center gap-2.5 px-3 py-2 text-sm text-foreground hover:bg-muted rounded-md mx-1 cursor-pointer outline-none transition-colors"
                    >
                      <Icon className="h-4 w-4 text-muted-foreground shrink-0" />
                      {label}
                    </Link>
                  </DropdownMenu.Item>
                ))}
              </DropdownMenu.Content>
            </DropdownMenu.Portal>
          </DropdownMenu.Root>

          <span className="hidden lg:block text-sm text-muted-foreground truncate max-w-40">
            {user.displayName || user.email}
          </span>
          <Button variant="ghost" size="sm" onClick={handleSignOut} className="gap-1.5">
            <LogOut className="h-4 w-4" />
            <span className="hidden sm:inline">Sign out</span>
          </Button>
        </div>
      </div>

      {/* Mobile bottom nav */}
      <nav className="sm:hidden flex border-t border-border">
        {navLinks.map(({ href, label, icon: Icon }) => (
          <Link
            key={href}
            href={href}
            className={`flex-1 flex flex-col items-center gap-0.5 py-2 text-xs font-medium transition-colors ${
              pathname === href ? 'text-foreground bg-muted' : 'text-muted-foreground'
            }`}
          >
            <Icon className="h-4 w-4" />
            {label}
          </Link>
        ))}

        {/* Mobile menu dropdown */}
        <DropdownMenu.Root>
          <DropdownMenu.Trigger asChild>
            <button className="flex-1 flex flex-col items-center gap-0.5 py-2 text-xs font-medium text-muted-foreground outline-none">
              <Menu className="h-4 w-4" />
              Menu
            </button>
          </DropdownMenu.Trigger>

          <DropdownMenu.Portal>
            <DropdownMenu.Content
              side="top"
              align="end"
              sideOffset={6}
              className="z-50 min-w-[180px] rounded-xl border border-border bg-card shadow-lg py-1.5 outline-none animate-in fade-in-0 zoom-in-95"
            >
              {infoLinks.map(({ href, label, icon: Icon }) => (
                <DropdownMenu.Item key={href} asChild>
                  <Link
                    href={href}
                    className="flex items-center gap-2.5 px-3 py-2 text-sm text-foreground hover:bg-muted rounded-md mx-1 cursor-pointer outline-none transition-colors"
                  >
                    <Icon className="h-4 w-4 text-muted-foreground shrink-0" />
                    {label}
                  </Link>
                </DropdownMenu.Item>
              ))}
            </DropdownMenu.Content>
          </DropdownMenu.Portal>
        </DropdownMenu.Root>
      </nav>
    </header>
  );
}
