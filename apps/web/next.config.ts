import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  transpilePackages: [
    "@portfolio/config",
    "@portfolio/schemas",
    "@portfolio/types",
    "@portfolio/ui",
    "@portfolio/utils"
  ]
};

export default nextConfig;
