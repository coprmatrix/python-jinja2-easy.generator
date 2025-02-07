if [ -z "$outdir" ]; then
  outdir='.'
fi
name="jinja2-easy.generator"
(
cd *"$name"
python3 -m build -s -n -o .
py2pack generate "$name" --localfile ./jinja2_easy.generator.egg-info/PKG-INFO --source-glob '%{name}-%{version}.tar.gz'
sed -i "s~^CHOOSE:.*~~; s~%{python_sitelib}/jinja2-easy\.generator.*~~; s~%files\(.*\)~%files \1\n%{python_sitelib}/jinja2_easy/\n%{python_sitelib}/jinja2_easy.generator-%{version}.dist-info/~; s/\(%autosetup.*\)jinja2-easy.generator\(.*\)/\1jinja2_easy_generator\2/g;" *.spec
)
mv *"$name"/*.{spec,tar.gz} "$outdir"/

