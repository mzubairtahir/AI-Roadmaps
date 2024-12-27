'use client';

import LoadingPage from "@/components/LoadingPage";
import Roadmap from "@/components/roadmap/Roadmap";
import WithAuthHoc from "@/hoc/WithAuthHoc";
import API from "@/utils/API";
import { useEffect, useState } from "react";


const RoadmapPage = ({ params }) => {
    const [roadmapData, setRoadmapData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [notFound, setNotFound] = useState(false);




    const fetchRoadmap = async () => {
        try {
            setLoading(true);
            const response = await API.getRoadmap(params.id);
            if (response.ok) {
                const data = await response.json();
                setRoadmapData(data);
            }
            else if (response.status === 404) {
                setNotFound(true);
            }
        }
        catch (error) {

        }
        finally {
            setLoading(false);

        }

    }

    useEffect(() => {
        (async function () {

            await fetchRoadmap();
        }());


    }, [])

    return <>
        <div>
            <div className="px-2 sm:px-14 my-2">
                {
                    loading ? <LoadingPage /> : null
                }
                {
                    notFound ? <p className="text-center">Could not find this roadmap!</p> : null
                }
                {
                    roadmapData ?
                        <Roadmap roadmapData={roadmapData} /> : null
                }

            </div>

        </div>


    </>


}


export default WithAuthHoc(RoadmapPage);