from pathlib import Path
import subprocess
import time
import random
#import gmcApp.magick_pdf_to_png
import latex.backtracking.backtracking_functions as btf
import datetime
import pytz


def merge_files(file1,file2,outputname):
    result = subprocess.run(["pdfunite", file1, file2, outputname])


def convert_to_pdf(tex_path, outputdir):
    result = subprocess.run(["latexmk","-outdir="+str(outputdir), tex_path])

# tex_keys = ['stepAB','stepABrev','boxA','boxB','boxBrev', 'boxArev' ]
tex_keys_ans = ["stepAB", "boxA", "boxBrev"]


def make1_diagram(tex_diagram_template_txt, num):
    tex_diagram_template_txt_ans = tex_diagram_template_txt
    posttext = r"\vspace{-2pt}"
    kv = btf.get_1step_process_dict(num)

    for key, value in kv.items():
        tex_diagram_template_txt_ans = tex_diagram_template_txt_ans.replace(
            "<<" + key + ">>", value
        )

    for key, value in kv.items():
        if key in tex_keys_ans:
            tex_diagram_template_txt = tex_diagram_template_txt.replace(
                "<<" + key + ">>", value
            )
        else:
            tex_diagram_template_txt = tex_diagram_template_txt.replace(
                "<<" + key + ">>", ""
            )

    # return tex_diagram_template_txt
    return tex_diagram_template_txt + posttext, tex_diagram_template_txt_ans + posttext


# def main():
    # num = input("Enter 1, 2, 3, 4 or 5 for +, -, X, /, random \n")
    # if num.strip().isdigit():
    #     num = int(num)
    #     if not num in [1, 2, 3, 4, 5]:
    #         num = 5  # random by default
    # else:
    #     num = 5  # random by default
    # filename = input("Enter the base filename to be added to the prefix bt1WS_: \n")
    # if not filename:
    #     filename = "bt1Bk_1st"  # "bt1Bk_1st_q and bt1Bk_1st_ans as default file"
    # # set names of files that are made
    # # questions
    # tex_output_path = currfile_dir_out / f"bt1Bk_{filename}_q.tex"
    # aux_path = currfile_dir_out / "temp"
    # # answers
    # tex_output_path_ans = currfile_dir_out / f"bt1Bk_{filename}_ans.tex"

    # # Read in the LaTeX template file
    # with open(tex_template_path, "r") as infile:
    #     tex_template_txt = infile.read()
    # # Read in the LaTeX template file for answers
    # with open(texans_template_path, "r") as infile:
    #     tex_template_txt_ans = infile.read()
    # # Read in the LaTeX diagram template file
    # with open(tex_diagram_template_path, "r") as infile:
    #     tex_diagram_template_txt = infile.read()

    # # <<cols>>
    # # generate column text and column text for answers
    # col1_text = ""
    # col1_text_ans = ""
    # for i in range(1, 21):
    #     img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, num)
    #     col1_text += img_tex
    #     col1_text_ans += img_tex_ans

    # # Replace the <<cols>> placeholder in the LaTeX template with the generated diagrams
    # tex_template_txt = tex_template_txt.replace("<<cols>>", col1_text)
    # tex_template_txt_ans = tex_template_txt_ans.replace("<<cols>>", col1_text_ans)

    # # Write the question tex to an output file
    # with open(tex_output_path, "w") as outfile:
    #     outfile.write(tex_template_txt)

    # # Write the answer tex to an output file
    # with open(tex_output_path_ans, "w") as outfile:
    #     outfile.write(tex_template_txt_ans)

    # # Wait for the file to be created
    # time.sleep(1)
    # # Convert the LaTeX files to PDFs
    # convert_to_pdf(tex_output_path,currfile_dir_out)
    # convert_to_pdf(tex_output_path_ans,currfile_dir_out)

    # tex_output_path_pdf = currfile_dir_out / f"bt1Bk_{filename}_q.pdf"
    # tex_output_path_ans_pdf = currfile_dir_out / f"bt1Bk_{filename}_ans.pdf"
    # tex_output_path_merged_pdf =currfile_dir_out / f"bt1Bk_{filename}_merged.pdf"\

    # merge_files(tex_output_path_pdf,tex_output_path_ans_pdf,tex_output_path_merged_pdf)


def create_booklet(num_q=20, num=5):
    currfile_dir = Path(__file__).parent
    timestamp = '{date:%Y%m%d_%H%M%S}'.format(date=datetime.datetime.now(tz=pytz.timezone("Australia/Melbourne")))
    currfile_dir_out = currfile_dir / "output" / timestamp
    Path(currfile_dir_out).mkdir(parents=True,exist_ok=True)
    tex_template_path = currfile_dir / "backtrack_1step_booklet_template.tex"
    texans_template_path = currfile_dir / "backtrack_1step_booklet_ans_template.tex"
    tex_diagram_template_path = (
        currfile_dir / "backtrack_1step_worksheet_diagram_template.tex"
    )
    # num = input("Enter 1, 2, 3, 4 or 5 for +, -, X, /, random \n")
    # if num.strip().isdigit():
    #     num = int(num)
    #     if not num in [1, 2, 3, 4, 5]:
    #         num = 5  # random by default
    # else:
    #     num = 5  # random by default
    #filename = input("Enter the base filename to be added to the prefix bt1WS_: \n")
    #if not filename:
    filename = "bt_" + timestamp  # "bt1Bk_1st_q and bt1Bk_1st_ans as default file"
    # set names of files that are made
    # questions
    tex_output_path = currfile_dir_out / f"{filename}_q.tex"
    aux_path = currfile_dir_out / "temp"
    # answers
    tex_output_path_ans = currfile_dir_out / f"{filename}_ans.tex"

    # Read in the LaTeX template file
    with open(tex_template_path, "r") as infile:
        tex_template_txt = infile.read()
    # Read in the LaTeX template file for answers
    with open(texans_template_path, "r") as infile:
        tex_template_txt_ans = infile.read()
    # Read in the LaTeX diagram template file
    with open(tex_diagram_template_path, "r") as infile:
        tex_diagram_template_txt = infile.read()

    # <<cols>>
    # generate column text and column text for answers
    col1_text = ""
    col1_text_ans = ""
    for i in range(1, num_q+1):
        img_tex, img_tex_ans = make1_diagram(tex_diagram_template_txt, num)
        col1_text += img_tex
        col1_text_ans += img_tex_ans

    # Replace the <<cols>> placeholder in the LaTeX template with the generated diagrams
    tex_template_txt = tex_template_txt.replace("<<cols>>", col1_text)
    tex_template_txt_ans = tex_template_txt_ans.replace("<<cols>>", col1_text_ans)

    # Write the question tex to an output file
    with open(tex_output_path, "w") as outfile:
        outfile.write(tex_template_txt)

    # Write the answer tex to an output file
    with open(tex_output_path_ans, "w") as outfile:
        outfile.write(tex_template_txt_ans)

    # Wait for the file to be created
    time.sleep(1)
    # Convert the LaTeX files to PDFs
    convert_to_pdf(tex_output_path,currfile_dir_out)
    convert_to_pdf(tex_output_path_ans,currfile_dir_out)

    tex_output_path_pdf = currfile_dir_out / f"{filename}_q.pdf"
    tex_output_path_ans_pdf = currfile_dir_out / f"{filename}_ans.pdf"
    tex_output_path_merged_pdf =currfile_dir_out / f"{filename}_merged.pdf"\

    merge_files(tex_output_path_pdf,tex_output_path_ans_pdf,tex_output_path_merged_pdf)

    return tex_output_path_merged_pdf

# if __name__ == "__main__":
#     print("starting")
#     main()
#     print("finished")
