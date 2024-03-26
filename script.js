import { compile, optimize, toSVG, showError } from "@penrose/core";
import trio from "./trio.js";

const compiled = await compile(trio);
// handle compilation errors
if (compiled.isErr()) {
  throw new Error(showError(compiled.error));
}
const converged = optimize(compiled.value);
// handle optimization errors
if (converged.isErr()) {
  throw new Error(showError(converged.error));
}
// render the diagram state as an SVG
const rendered = await toSVG(converged.value, async () => undefined);
const container = document.getElementById("diagram");
container.appendChild(rendered);