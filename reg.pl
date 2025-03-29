my $name = <<'EOF';
%files -n %{python_name}
%{python3_sitelib}/*.dist-info
%{python3_sitelib}/jinja2_easy/__pycache__/*
%{python3_sitelib}/jinja2_easy/generator.py
EOF

s/%files -n %{python_name}.*/${name}/g;
