const BASE = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://127.0.0.1:8000/api'


export async function api<T>(path: string, init?: RequestInit): Promise<T> {
const res = await fetch(`${BASE}${path}`, {
    ...init,
    headers: {
        'Content-Type': 'application/json',
        ...(init?.headers || {})
    },
    // Next.js 캐시 정책은 필요시 조정
    cache: 'no-store'
    })
    if (!res.ok) {
        const text = await res.text()
        throw new Error(`API ${path} failed: ${res.status} ${text}`)
    }
return res.json() as Promise<T>
}