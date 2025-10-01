'use client'
import Link from 'next/link'
import { ShoppingCart, Search } from 'lucide-react'


export default function Header() {
    return (
        <header className="border-b">
            <div className="container h-14 flex items-center justify-between">
                <Link href="/" className="font-bold">AIMS Store</Link>
                <div className="flex items-center gap-3">
                    <div className="hidden md:flex items-center gap-2 border rounded-xl px-3 py-1.5">
                    <Search className="w-4 h-4" />
                    <input className="outline-none" placeholder="검색" />
                    </div>
                    
                    <Link href="/cart" className="inline-flex items-center gap-2">
                    <ShoppingCart className="w-5 h-5" />
                    <span className="hidden md:inline">장바구니</span>
                    </Link>
                </div>
            </div>
        </header>
    )
}