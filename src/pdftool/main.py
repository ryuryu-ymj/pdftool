from pathlib import Path

import pymupdf as mu
import click


@click.group()
def main():
    pass


@main.command(help="Compress PDF file size.")
@click.argument("src", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.argument("out", required=False, type=click.Path(path_type=Path))
def compress(src: str, out: str):
    if out is None:
        out = Path(src.stem + "_compress.pdf")
    click.echo(f"Compress {src} to {out}.")

    doc = mu.open(src)

    doc.save(
        out,
        garbage=4,
        clean=True,
        deflate=True,
        deflate_images=True,
        deflate_fonts=True,
    )

    doc.close()


@main.command(help="Resize PDF pages.")
@click.argument("src", type=click.Path(exists=True, dir_okay=False, path_type=Path))
@click.argument("out", required=False, type=click.Path(path_type=Path))
@click.option(
    "--paper",
    type=click.Choice(
        sum(
            [
                [f"{s}", f"{s}-l"]
                for s in (
                    [f"{ab}{n}" for ab in ["A", "B", "C"] for n in range(1, 11)]
                    + [
                        "Card-4x6",
                        "Card-5x7",
                        "Commercial",
                        "Executive",
                        "Invoice",
                        "Ledger",
                        "Legal",
                        "Legal-13",
                        "Letter",
                        "Monarch",
                        "Tabloid-Extra",
                    ]
                )
            ],
            [],
        ),
        case_sensitive=False,
    ),
    default="A4",
    show_default=True,
    help="Page size of the output PDF.",
)
@click.option(
    "--compress",
    type=click.BOOL,
    default=True,
    show_default=True,
    help="Compress the output PDF.",
)
def resize(src: Path, out: Path, paper: str, compress: bool):
    if out is None:
        out = Path(src.stem + "_resize.pdf")
    click.echo(f"Resize {src} to {out}.")

    src = mu.open(src)
    doc = mu.open()
    for ipage in src:
        if ipage.rect.width > ipage.rect.height:
            fmt = mu.paper_rect("a4-l")  # landscape if input suggests
        else:
            fmt = mu.paper_rect(paper)
        page = doc.new_page(width=fmt.width, height=fmt.height)
        page.show_pdf_page(page.rect, src, ipage.number)

    if compress:
        doc.save(
            out,
            garbage=4,
            clean=True,
            deflate=True,
            deflate_images=True,
            deflate_fonts=True,
        )
    else:
        doc.save(out, garbage=4)

    src.close()
    doc.close()
