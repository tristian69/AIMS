import './globals.css'
import { ReactNode } from 'react'
import Header from '@/components/Header'
import Footer from '@/components/Footer'


export const metadata = {
    title: 'AIMS Store',
    description: 'Next.js + Django E‑commerce'
}


export default function RootLayout({ children }: { children: ReactNode }) {
    return (
        <html lang="ko">
            <body>
                <Header />
                    <main className="min-h-[70vh] container py-6">{children}</main>
                <Footer />
            </body>
        </html>
    )
}