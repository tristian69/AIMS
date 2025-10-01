import { api } from '@/lib/api'
import type { Product } from '@/lib/types'


export default async function ProductDetail({ params }: { params: { slug: string } }) {
    const product = await api<Product>(`/products/${params.slug}/`)
    return (
        <div className="grid md:grid-cols-2 gap-6">
            <div>
                {/* 간단한 이미지 갤러리 */}
                <img className="w-full rounded-xl border" src={product.images?.[0]?.url || 'https://placehold.co/800x600'} alt={product.title} />
            </div>
            <div>
                <h1 className="text-2xl font-semibold">{product.title}</h1>
                <p className="text-gray-600 mt-2">{product.brand}</p>
                <p className="text-xl font-bold mt-4">₩{product.price}</p>
                <p className="mt-4 text-gray-700 whitespace-pre-line">{product.description}</p>
                <button className="mt-6 px-4 py-2 rounded-xl bg-black text-white">장바구니 담기</button>
            </div>
        </div>
    )
}