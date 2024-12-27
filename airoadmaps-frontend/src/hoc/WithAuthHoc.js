'use client';

import { useUser } from "@/context/UserContext";
import { usePathname, useRouter } from "next/navigation";


const WithAuthHoc = (WrappedComponent) => {


    return (props) => {
        const { user } = useUser();
        const router = useRouter();
        const path = usePathname();


        if (!user.loggedIn) {
            router.push(`/auth?next=${path}`);
            return
        }


        return <WrappedComponent {...props} />


    }

}

export default WithAuthHoc;

