import { Button } from "@/components/ui/button";

export default function Home() {
  return (
    <div className="flex flex-col flex-1">
    <main className="flex  justify-center">
      <h1 className="text-6xl font-bold"></h1>
    </main>
    <footer className="footer pd-6 px-6 relative mb-0">
      <Button>Start</Button>
    </footer>
    </div>
  )
}
