'use client'

import LoadingPage from "@/components/LoadingPage";
import WithAuthHoc from "@/hoc/WithAuthHoc"
import Link from "next/link";
import { useEffect, useState } from "react"


const RoadmapItem = ({ roadmapData, deleteFunction, index }) => {
    const [deleting, setDeleting] = useState(false);

    const deleteFunctionWrapper = async () => {
        setDeleting(true);
        await deleteFunction(index);
        setDeleting(false);



    }

    return <div className="flex items-center bg-white text-black px-4 my-2 py-2 rounded">
        <Link href={`/roadmap/${roadmapData.id}`} className="cursor-pointer  w-full py-4 flex justify-between items-center">
            <div className="font-bold">{roadmapData.title}</div>
        </Link>
        <div className="px-2"><button disabled={deleting} onClick={() => deleteFunctionWrapper()} className="p-1.5 bg-red-500 hover:bg-red-600">{deleting ? "Deleting" : "Delete"}</button></div>
    </div>
}

const RoadmapsPage = () => {

    const [roadmapsData, setRoadmapsData] = useState([]);
    const [loading, setLoading] = useState(true);

    const deleteRoadmap = async (index) => {
        const roadmap = roadmapsData[index];
        if (!roadmap) {
            return;
        }
        await (async function () {
            try {
                const response = await fetch(`/api/roadmap/${roadmap.id}`, {
                    method: "delete"
                })
                if (response.ok) {
                    setRoadmapsData((preData) => preData.filter((elem, ind) => index !== ind));
                }
            }
            catch (error) {
            }


        }());

    }

    useEffect(() => {

        (async function () {
            const response = await fetch("/api/roadmap/list")
            if (response.ok) {
                setRoadmapsData(await response.json());
            }
            else {
                return;
            }

            setLoading(false);

        }());


    }, [])

    if (loading) {
        return loading ? <LoadingPage /> : null
    }
    return <div>
        <div className="px-2 sm:px-14 my-2">
            {
                roadmapsData.length === 0 ? <p className="text-center">You dont have any roadmap yet!</p> : null
            }
            {
                roadmapsData.length !== 0 ? roadmapsData.map((element, index) => {
                    return <RoadmapItem deleteFunction={deleteRoadmap} index={index} key={index} roadmapData={element} />

                }) : null

            }

        </div>

    </div>


}

export default WithAuthHoc(RoadmapsPage);