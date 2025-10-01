import type { NextConfig } from 'next'


const nextConfig: NextConfig = {
    reactStrictMode: true,
    images: {
        remotePatterns: [
            { protocol: 'https', hostname: '**.amazonaws.com' },
            { protocol: 'https', hostname: '**.cloudfront.net' },
            { protocol: 'http', hostname: '127.0.0.1' },
            { protocol: 'http', hostname: 'localhost' }
        ]
    },
    experimental: {
    // 최신 Next 기능 사용 시 필요에 따라 옵션 추가
    }
}
export default nextConfig