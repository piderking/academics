import pypdf
import os
import glob

midterm2_dir = r"G:\My Drive\Academics\BOT-1121 (1)\Midterm 2"
pdf_files = sorted(glob.glob(os.path.join(midterm2_dir, "*.pdf")))

print(f"Found {len(pdf_files)} PDF files in Midterm 2 folder:\n")

summary = {}
for pdf_path in pdf_files:
    fname = os.path.basename(pdf_path)
    try:
        reader = pypdf.PdfReader(pdf_path)
        num_pages = len(reader.pages)
        
        # sample text from first 5 pages and middle pages
        sample_text = ""
        for p in range(min(5, num_pages)):
            txt = reader.pages[p].extract_text() or ""
            sample_text += f"\n[P{p+1}] " + txt[:200].replace('\n', ' ')
            
        summary[fname] = {
            "pages": num_pages,
            "sample": sample_text[:600]
        }
        print(f"=== {fname} ({num_pages} pages) ===")
        print(summary[fname]["sample"][:300] + "...\n")
    except Exception as e:
        print(f"Error reading {fname}: {e}")
