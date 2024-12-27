'use client'


import Conversation from "@/components/conversation/Conversation";
import CreatePageSection from "@/components/CreatePageSection";
import WithAuthHoc from "@/hoc/WithAuthHoc";
import API from "@/utils/API";

import { useRouter } from "next/navigation";
import { useEffect, useState } from "react"




const CreatePage = () => {

    const [generating, setGenerating] = useState(false);
    const [messages, setMessages] = useState([]);
    const router = useRouter();


    useEffect(() => {
        window.scrollBy(document.body.scrollTop, document.body.scrollHeight)


    }, [messages])


    useEffect(() => {
        (async function () {


            if (generating) {
                const resposne = await API.createRoadmap(messages);
                if (resposne && resposne.ok) {
                    const json = await resposne.json();
                    if (json.created) {
                        // roadmap is created 
                        router.push(`/roadmap/${json.course_id}`)
                    }
                    else {
                        setGenerating(false)
                        setMessages((prevMessages) => [...prevMessages, { "role": "assistant", "content": json.message }])

                    }

                }


            }
        })();


    }, [generating])


    const sendMessage = async (event) => {
        event.preventDefault();
        if (generating) {
            return;
        }

        const inputValue = event.target.input.value;
        if (inputValue.length === 0) {
            return;
        }


        setGenerating(true);
        setMessages((prevMessages) => [...prevMessages, { "role": "user", "content": inputValue }])
        event.target.reset();


    }





    return <>
        <div>
            {messages.length === 0 ? <CreatePageSection />
                :
                <div className="mb-16">
                    <Conversation messages={messages} />
                    <div className="pb-6">
                        <div className="pb-8 text-center text-lg font-bold">
                            {generating ? "Agent is thinking..." : null}
                        </div>
                    </div>

                </div>

            }



            <div>
                <div className="bg-background fixed py-2 pb-6 block left-0 bottom-0 right-0 flex justify-center">

                    <form onSubmit={sendMessage} className=" rounded inline-block">

                        <input
                            className="p-1.5 rounded bg-white border border-gray-300 focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500  text-gray-800 placeholder-gray-400 shadow-sm"
                            type="text"
                            placeholder="Enter your message"
                            name="input"
                        />

                        <button disabled={generating ? true : false} type="submit" className="p-2">Send</button>
                    </form>
                </div>
            </div>

        </div>

    </>

}


export default WithAuthHoc(CreatePage);