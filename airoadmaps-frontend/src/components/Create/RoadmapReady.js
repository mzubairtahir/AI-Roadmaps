import CloseIcon from "../Svg/CloseIcon";


export default function RoadmapReady({ closeFunction }) {

    return <>
        <div className="fixed left-4 bottom-4 bg-[var(--foreground)] text-black p-2 rounded">
            Your Roadmap is ready.
            <span className="text-[var(--accent)] mx-1.5">
                <a href="#" className="underline">
                    View
                </a>
            </span>
            <span className="mx-2">
                <button onClick={closeFunction} className="bg-transparent">
                    <CloseIcon fill="black" className="w-4 inline" />
                </button>
            </span>
        </div>
    </>

}