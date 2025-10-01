import type { Config } from 'tailwindcss'

export default {
    content: [
        './src/app/**/*.{ts,tsx}',
        './src/components/**/*.{ts,tsx}',
        '../../packages/ui/src/**/*.{ts,tsx}'
    ],
    theme: {
        extend: {
            container: { center: true, padding: '1rem' }
        }
    },
    plugins: []
} satisfies Config