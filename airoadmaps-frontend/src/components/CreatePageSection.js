import { useState } from "react"
import Help from "@/components/Create/Help";

const CreatePageSection = () => {
    const [showHelp, setShowHelp] = useState(false);

    return <>
        <div className="flex justify-center flex-column items-center flex-col py-12 my-7">

            <div className="text-center">
                <div>

                    <h1>Create Your Roadmap</h1>
                </div>
            </div>
            <div className="relative group inline-block">
                <button onClick={() => setShowHelp(true)} className="text-white bg-transparent">
                    <svg fill="white" className="w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
                        <path d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM216 336l24 0 0-64-24 0c-13.3 0-24-10.7-24-24s10.7-24 24-24l48 0c13.3 0 24 10.7 24 24l0 88 8 0c13.3 0 24 10.7 24 24s-10.7 24-24 24l-80 0c-13.3 0-24-10.7-24-24s10.7-24 24-24zm40-208a32 32 0 1 1 0 64 32 32 0 1 1 0-64z" /></svg>
                </button>

            </div>
        </div>
        {showHelp ? <Help closeHelp={() => setShowHelp(false)} /> : null}


    </>
}

export default CreatePageSection;