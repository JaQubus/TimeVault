import { HTMLProps } from "react";

type LogoProps = HTMLProps<SVGSVGElement>;

export default function Logo(props: LogoProps) {
  return (
    <svg
      {...props}
      viewBox="0 0 22 28"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M20.3333 27.3333H21.6666V24.6667H20.3333V23.3333C20.3307 21.7136 19.9075 20.1222 19.1051 18.7152C18.3027 17.3081 17.1487 16.1336 15.7559 15.3067C15.2826 15.0267 14.9999 14.5773 14.9999 14.1053V13.8947C14.9999 13.4227 15.2826 12.9733 15.7546 12.6947C17.1476 11.8675 18.3019 10.6928 19.1045 9.28557C19.9072 7.8783 20.3305 6.28672 20.3333 4.66666V3.33332H21.6666V0.666656H0.333252V3.33332H1.66659V4.66666C1.66929 6.28672 2.09268 7.8783 2.8953 9.28557C3.69791 10.6928 4.85224 11.8675 6.24525 12.6947C6.71725 12.9733 6.99992 13.4213 6.99992 13.8947V14.1053C6.99992 14.5773 6.71725 15.0267 6.24525 15.3053C4.85224 16.1324 3.69791 17.3071 2.8953 18.7144C2.09268 20.1217 1.66929 21.7133 1.66659 23.3333V24.6667H0.333252V27.3333H20.3333ZM17.6666 3.33332V4.66666C17.6646 6.10965 17.1949 7.51312 16.3279 8.66666H5.67192C4.80496 7.51312 4.33527 6.10965 4.33325 4.66666V3.33332H17.6666ZM7.59992 17.6027C8.89458 16.8373 9.66658 15.5307 9.66658 14.1053V14H12.3333V14.1053C12.3333 15.5293 13.1053 16.8373 14.4013 17.6027C15.5993 18.3156 16.5425 19.3876 17.0972 20.6667H4.90259C5.45742 19.3873 6.4012 18.3152 7.59992 17.6027Z"
        fill="url(#paint0_linear_6_266)"
      />
      <defs>
        <linearGradient
          id="paint0_linear_6_266"
          x1="10.9999"
          y1="0.666656"
          x2="10.9999"
          y2="27.3333"
          gradientUnits="userSpaceOnUse"
        >
          <stop stopColor="white" />
          <stop offset="1" stopColor="#727272" />
        </linearGradient>
      </defs>
    </svg>
  );
}

