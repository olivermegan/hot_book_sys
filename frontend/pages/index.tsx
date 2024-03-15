import Image from "next/image";
import { Inter } from "next/font/google";
import { gql, useQuery } from "@apollo/client";

const inter = Inter({ subsets: ["latin"] });

type Booking = {
  checkIn: string;
  guest: string;
  price: string;
  checkOut: string;
  status: string;
};

export default function Home() {
  const GET_BOOKING = gql`
    query GetBooking {
      booking {
        checkIn
        guest
        price
        checkOut
        status
      }
    }
  `;

  const { data } = useQuery(GET_BOOKING);
  if (!data) return null;
  return (
    <main
      className={`flex min-h-screen flex-col items-center justify-between p-24 ${inter.className}`}
    >
      {data.booking.map((booking: Booking) => {
        return (
          <div
            key={booking.price}
            className="bg-gray-100 p-4 rounded-lg shadow-md mb-4"
          >
            <p className="text-blue-700 mb-1">Guest: {booking.guest}</p>
            <p className="text-blue-700 mb-1">Price: ${booking.price}</p>
            <p className="text-blue-700 mb-1">Check-In: {booking.checkIn}</p>
            <p className="text-blue-700 mb-1">Check-Out: {booking.checkOut}</p>
            <p className="text-blue-700 mb-1">Status: {booking.status}</p>
          </div>
        );
      })}
    </main>
  );
}
