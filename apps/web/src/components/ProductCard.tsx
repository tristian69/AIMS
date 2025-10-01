import Link from 'next/link'
import type { Product } from '@/lib/types'


export default function ProductCard({ product }: { product: Product }) {
    return (
        <Link href={`/products/${product.slug}`} className="block group">
        <div className="aspect-[4/3] rounded-xl overflow-hidden border">
            <img
            src={product.images?.[0]?.url || 'https://placehold.co/600x450'}
            alt={product.title}
            className="w-full h-full object-cover group-hover:scale-105 transition"
            />
        </div>
        <div className="mt-2">
            <h3 className="text-sm text-gray-700 line-clamp-1">{product.title}</h3>
            <div className="font-semibold">₩{product.price}</div>
        </div>
        </Link>
    )
}