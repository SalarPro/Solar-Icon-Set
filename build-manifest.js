#!/usr/bin/env node
/**
 * Build script to generate icon manifest for the Solar Icon Gallery
 * Run: node build-manifest.js
 */

const fs = require('fs');
const path = require('path');

const ICONS_DIR = path.join(__dirname, 'icons', 'solar');
const OUTPUT_FILE = path.join(__dirname, 'manifest.json');

// Icon types to scan
const ICON_TYPES = ['bold', 'bold_duotone', 'broken', 'line_duotone', 'linear', 'outline'];

function scanIcons() {
    const icons = [];
    
    for (const type of ICON_TYPES) {
        const typePath = path.join(ICONS_DIR, type);
        
        if (!fs.existsSync(typePath)) {
            console.warn(`Warning: Type folder not found: ${type}`);
            continue;
        }
        
        const categories = fs.readdirSync(typePath, { withFileTypes: true })
            .filter(d => d.isDirectory() && !d.name.startsWith('sp_')) // Skip sp_ folders
            .map(d => d.name);
        
        for (const category of categories) {
            const categoryPath = path.join(typePath, category);
            
            try {
                const files = fs.readdirSync(categoryPath)
                    .filter(f => f.endsWith('.svg'));
                
                for (const file of files) {
                    const name = file.replace('.svg', '');
                    icons.push({
                        path: `icons/solar/${type}/${category}/${file}`,
                        type,
                        category,
                        name
                    });
                }
            } catch (err) {
                console.warn(`Warning: Could not read ${categoryPath}: ${err.message}`);
            }
        }
    }
    
    return icons;
}

function main() {
    console.log('Scanning icons...');
    const icons = scanIcons();
    
    // Get unique categories and types for metadata
    const types = [...new Set(icons.map(i => i.type))].sort();
    const categories = [...new Set(icons.map(i => i.category))].sort();
    
    const manifest = {
        generated: new Date().toISOString(),
        totalCount: icons.length,
        types,
        categories,
        icons
    };
    
    fs.writeFileSync(OUTPUT_FILE, JSON.stringify(manifest, null, 2));
    
    console.log(`✓ Generated manifest.json`);
    console.log(`  - Total icons: ${icons.length}`);
    console.log(`  - Types: ${types.length}`);
    console.log(`  - Categories: ${categories.length}`);
}

main();
