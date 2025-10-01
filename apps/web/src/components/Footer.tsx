export default function Footer() {
    return (
        <footer className="border-t mt-12">
            <div className="container h-16 flex items-center justify-between text-sm text-gray-500">
                <p>© {new Date().getFullYear()} AIMS</p>
                <p className="hidden md:block">Powered by Next.js & Django</p>
            </div>
        </footer>
    )
}