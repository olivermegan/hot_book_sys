import Image from "next/image";
import { Inter } from "next/font/google";
import { gql, useQuery } from "@apollo/client";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  const GET_BOOKING = gql`
    query GetBooking {
      booking {
        checkIn
        guest
        price
      }
    }
  `;

  const { data } = useQuery(GET_BOOKING);

  return (
    <main
      className={`flex min-h-screen flex-col items-center justify-between p-24 ${inter.className}`}
    >
      <div>{JSON.stringify(data)}</div>
    </main>
  );
}
