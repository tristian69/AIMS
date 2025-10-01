import { ButtonHTMLAttributes } from 'react'


export default function Button({ className = '', ...props }: ButtonHTMLAttributes<HTMLButtonElement>) {
    return (
        <button
        {...props}
        className={`px-4 py-2 rounded-xl border bg-white hover:bg-gray-50 active:translate-y-px ${className}`}
        />
    )
}