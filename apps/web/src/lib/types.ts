export type Category = {
    id: number
    name: string
    slug: string
    description?: string
}


export type ProductImage = { id: number; url: string }


export type Variant = {
    id: number
    sku: string
    price: string
    stock: number
    attributes?: Record<string, string>
}


export type Product = {
    id: number
    title: string
    slug: string
    description?: string
    brand?: string
    price: string
    category: Category
    images: ProductImage[]
    variants: Variant[]
}