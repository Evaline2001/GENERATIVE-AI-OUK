import streamlit as st
import os, subprocess

st.title("💡 Codebase Genius – Auto Documentation Tool")

repo_url = st.text_input("Enter a GitHub repository URL:")

if st.button("Generate Documentation"):
    if repo_url.strip():
        st.info("Processing... please wait ⏳")
        cmd = f"jsctl run main.jac -walk code_genius.run --ctx '{{\"repo_url\":\"{repo_url}\"}}'"
        process = subprocess.Popen(cmd, shell=True,
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        st.text(out.decode())
        if os.path.exists("docs.md"):
            st.success("✅ Documentation generated successfully!")
            with open("docs.md", "r") as f:
                st.download_button("Download docs.md", data=f.read(), file_name="docs.md")
            if os.path.exists("graph.png"):
                st.image("graph.png", caption="Code Relationship Graph")
        else:
            st.error("❌ Generation failed.")
    else:
        st.warning("Please enter a valid GitHub URL.")
