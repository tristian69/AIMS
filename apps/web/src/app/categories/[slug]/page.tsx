import { api } from '@/lib/api'
import type { Product } from '@/lib/types'
import ProductCard from '@/components/ProductCard'


export default async function CategoryPage({ params, searchParams }: { params: { slug: string }, searchParams: { q?: string } }) {
    const q = searchParams?.q ? `&q=${encodeURIComponent(searchParams.q)}` : ''
    const products = await api<Product[]>(`/products/?category=${params.slug}${q}`)
    return (
        <div className="space-y-6">
        <h1 className="text-2xl font-semibold">카테고리: {params.slug}</h1>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                {products.map((p) => (
                <ProductCard key={p.id} product={p} />
                ))}
            </div>
        </div>
    )
}