import { api } from '@/lib/api'
import type { Product } from '@/lib/types'
import ProductCard from '@/components/ProductCard'


export default async function HomePage() {
    const products = await api<Product[]>('/products/?limit=8')
    return (
        <div className="space-y-6">
            <h1 className="text-2xl font-semibold">추천 상품</h1>
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                {products.map((p) => (
                <ProductCard key={p.id} product={p} />)
                )}
            </div>
        </div>
    )
}