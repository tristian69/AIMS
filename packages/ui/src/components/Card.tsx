import { HTMLAttributes } from 'react'


export default function Card({ className = '', ...props }: HTMLAttributes<HTMLDivElement>) {
    return <div {...props} className={`rounded-2xl border p-4 bg-white ${className}`} />
}