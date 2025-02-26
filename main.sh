if [ -z "$outdir" ]; then
  outdir='.'
fi
name="jinja2-easy.generator"
(
cd *"$name"
python3 -m build -s -n -o .
py2pack generate "$name" --localfile ./jinja2_easy.generator.egg-info/PKG-INFO --source-glob '%{name}-%{version}.tar.gz'

sed -i "s~%{pypi_name}-%{version}~jinja2_easy_generator-%{version}~;" *.spec
)
mv *"$name"/*.{spec,tar.gz} "$outdir"/

