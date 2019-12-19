# -*- coding: utf-8 -*-

import coffice

def migrate(cr, version):
    registry = coffice.registry(cr.dbname)
    from coffice.addons.account.models.chart_template import migrate_set_tags_and_taxes_updatable
    migrate_set_tags_and_taxes_updatable(cr, registry, 'l10n_nl')
