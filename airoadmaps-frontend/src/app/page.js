'use client';

import Head from 'next/head';
import Link from 'next/link';

function Home() {


  return <>
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-900 text-gray-100">
      <Head>
        <title>AI Roadmap Generator</title>
        <meta name="description" content="AI Roadmap Generator - by self learner for self learner" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className="text-center">
        <h1 className="text-4xl font-bold mb-4">AI Roadmap Generator</h1>
        <p className="text-lg mb-8">By self learner for self learner</p>
        <Link href="/create" className="mt-6 inline-block px-6 py-3 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 transition">
          Get Started
        </Link>
      </main>

    </div>
  </>

}

export default Home;