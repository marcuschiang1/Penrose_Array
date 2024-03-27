import { fetchResolver } from "@penrose/components";
import { diagram } from "@penrose/core";
import trio from "./trio.js";

await diagram(trio, document.getElementById("diagram"), fetchResolver);